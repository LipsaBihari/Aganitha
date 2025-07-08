import argparse
from pubmed_fetcher.fetcher import fetch_papers, filter_results, save_to_csv


def main():
    parser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed with at least one non-academic (industry) author."
    )

    # Required positional query argument
    parser.add_argument(
        "query",
        type=str,
        help="Search query string for PubMed. Wrap in quotes if it contains spaces."
    )

    # Optional CSV output flag
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Output filename for saving results as CSV. If not provided, results will be printed to console."
    )

    # Optional debug flag
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug logging during execution."
    )

    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] Starting PubMed fetch for query:", args.query)

    xml_data = fetch_papers(args.query, debug=args.debug)

    if not xml_data:
        print("[ERROR] No data returned. Check your internet connection or query.")
        return

    results = filter_results(xml_data, debug=args.debug)

    if not results:
        print("[INFO] No qualifying research papers found.")
        return

    if args.file:
        save_to_csv(results, args.file)
        print(f"[SUCCESS] Results saved to {args.file}")
    else:
        print("[RESULTS]")
        for i, paper in enumerate(results, 1):
            print(f"\n--- Paper #{i} ---")
            for key, value in paper.items():
                print(f"{key}: {value}")
        print("\n[END]")


if __name__ == "__main__":
    main()
