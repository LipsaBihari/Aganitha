import requests
import pandas as pd
import xml.etree.ElementTree as ET
from typing import List, Dict
from pubmed_fetcher.utils import is_non_academic, extract_email


def fetch_papers(query: str, debug: bool = False) -> str:
    """
    Fetches PubMed XML data for a given search query.

    Args:
        query (str): The PubMed search term.
        debug (bool): Whether to print debug information.

    Returns:
        str: XML response from PubMed EFetch API.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    # Step 1: Search
    search_url = f"{base_url}esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50
    }

    try:
        search_response = requests.get(search_url, params=search_params)
        search_response.raise_for_status()
        if debug:
            print("[DEBUG] Search URL:", search_response.url)

        ids = search_response.json()["esearchresult"].get("idlist", [])
        if not ids:
            return ""

        # Step 2: Fetch paper details
        fetch_url = f"{base_url}efetch.fcgi"
        fetch_params = {
            "db": "pubmed",
            "id": ",".join(ids),
            "retmode": "xml"
        }

        fetch_response = requests.get(fetch_url, params=fetch_params)
        fetch_response.raise_for_status()
        if debug:
            print("[DEBUG] Fetch URL:", fetch_response.url)

        return fetch_response.text

    except requests.RequestException as e:
        if debug:
            print("[ERROR] API request failed:", e)
        return ""


def filter_results(xml_data: str, debug: bool = False) -> List[Dict]:
    """
    Filters the XML data to extract relevant research papers with non-academic authors.

    Args:
        xml_data (str): Raw XML string from PubMed.
        debug (bool): Whether to print debug information.

    Returns:
        List[Dict]: Filtered paper details.
    """
    results = []

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        if debug:
            print("[ERROR] Failed to parse XML:", e)
        return []

    for article in root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"

            authors = article.findall(".//Author")
            non_academic_authors = []
            companies = []
            email = None

            for author in authors:
                affil = author.findtext(".//AffiliationInfo/Affiliation")
                if affil:
                    if is_non_academic(affil):
                        name = f"{author.findtext('ForeName') or ''} {author.findtext('LastName') or ''}".strip()
                        non_academic_authors.append(name)
                        companies.append(affil)

                    if not email:
                        email = extract_email(affil)

            if non_academic_authors:
                results.append({
                    "PubmedID": pmid,
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": "; ".join(non_academic_authors),
                    "Company Affiliation(s)": "; ".join(companies),
                    "Corresponding Author Email": email or "Not Found"
                })

        except Exception as e:
            if debug:
                print("[WARNING] Skipping article due to error:", e)

    return results


def save_to_csv(results: List[Dict], filename: str):
    """
    Saves the filtered research paper data to a CSV file.

    Args:
        results (List[Dict]): List of filtered paper details.
        filename (str): Path to the output CSV file.
    """
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
