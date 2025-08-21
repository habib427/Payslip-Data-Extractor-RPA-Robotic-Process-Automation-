import pandas as pd

def export_to_excel(data_list, output_file="output/extracted_data.xlsx"):
    df = pd.DataFrame(data_list)
    df.to_excel(output_file, index=False)
    print("Data exported to {output_file}")
