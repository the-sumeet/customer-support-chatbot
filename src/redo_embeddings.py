from pathlib import Path

from src.tools.embeddings import create_vector_store, load_vector_store
from src.tools.rag import setup_rag_chain
from src.tools.source import load_documents


def main():
    path = Path(__file__).parent.parent / "source"
    pdf_paths = [
        path / "America's_Choice_2500_Gold_SOB (1) (1).pdf",
        path / "America's_Choice_5000_Bronze_SOB (2).pdf",
        path / "America's_Choice_5000_HSA_SOB (2).pdf",
        path / "America's_Choice_7350_Copper_SOB (1) (1).pdf",
    ]

    docs_paths = [
        path / "America's_Choice_Medical_Questions_-_Modified_(3) (1).docx",

    ]
    website_urls = [
        "https://www.angelone.in/support/add-and-withdraw-funds/add-funds",
        "https://www.angelone.in/support/angel-one-recommendations/charges-and-frequency",
        "https://www.angelone.in/support/charges-and-cashbacks/dp-charges",
        "https://www.angelone.in/support/charts/chart-not-loading",
        "https://www.angelone.in/support/complaince/trading-surveillance",
        "https://www.angelone.in/support/fixed-deposits/account-verification",
        "https://www.angelone.in/support/ipo-ofs/ipo",
        "https://www.angelone.in/support/loans/active-loans",
        "https://www.angelone.in/support/margin-pledging-and-margin-trading-facility/available-margin-to-trade",
        "https://www.angelone.in/support/mutual-funds/orders",
        "https://www.angelone.in/support/portfolio-and-corporate-actions/bonus-issue",
        "https://www.angelone.in/support/reports-and-statements/client-master-list",
"https://www.angelone.in/support/your-account/family-declaration",
        "https://www.angelone.in/support/your-orders/watchlist",
    ]

    documents = load_documents(pdf_paths, docs_paths, website_urls)

    create_vector_store(documents)

if __name__ == "__main__":
    main()