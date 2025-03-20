import random
import datetime
import pandas as pd

# List of sample products
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"]


def generate_report():
    report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_data = []

    total_revenue = 0
    for product in products:
        quantity_sold = random.randint(10, 500)  # Random quantity sold
        price_per_unit = random.uniform(50.0, 1000.0)  # Random price
        revenue = quantity_sold * price_per_unit
        total_revenue += revenue

        report_data.append(
            {
                "Product": product,
                "Quantity Sold": quantity_sold,
                "Price per Unit (USD)": round(price_per_unit, 2),
                "Revenue (USD)": round(revenue, 2),
            }
        )

    # Add total revenue as a summary row
    report_data.append(
        {
            "Product": "Total",
            "Quantity Sold": "",
            "Price per Unit (USD)": "",
            "Revenue (USD)": round(total_revenue, 2),
        }
    )

    # Create a DataFrame
    df = pd.DataFrame(report_data)

    # Save DataFrame to an Excel file
    file_name = "sales_report.csv"
    df.to_csv(file_name, index=False)
    print(f"Sales report saved as '{file_name}'.")


# Run the script
if __name__ == "__main__":
    generate_report()
