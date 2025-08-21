import re

def clean_payslip_data(raw_text: str) -> dict:
    data = {}

    data["employee_code"] = re.search(r"Employee Code\s*:\s*(\S+)", raw_text)
    data["employee_code"] = data["employee_code"].group(1) if data["employee_code"] else ""

    data["employee_name"] = re.search(r"Employee Name\s*:\s*(.+?)\s+Station", raw_text)
    data["employee_name"] = data["employee_name"].group(1).strip() if data["employee_name"] else ""

    data["station"] = re.search(r"Station\s*:\s*(.+?)\s+Department", raw_text)
    data["station"] = data["station"].group(1).strip() if data["station"] else ""

    data["department"] = re.search(r"Department\s*:\s*(.+?)\s+Sub Department", raw_text)
    data["department"] = data["department"].group(1).strip() if data["department"] else ""

    data["designation"] = re.search(r"Designation\s*:\s*(.+?)\s+CnicNo", raw_text)
    data["designation"] = data["designation"].group(1).strip() if data["designation"] else ""

    data["cnic"] = re.search(r"CnicNo\s*:\s*([\d-]+)", raw_text)
    data["cnic"] = data["cnic"].group(1) if data["cnic"] else ""

    data["joining_date"] = re.search(r"Joining Date\s*:\s*(.+?)\s+Monthly Salary", raw_text)
    data["joining_date"] = data["joining_date"].group(1).strip() if data["joining_date"] else ""

    data["monthly_salary"] = re.search(r"Monthly Salary\s*:\s*([\d,]+)", raw_text)
    data["monthly_salary"] = data["monthly_salary"].group(1) if data["monthly_salary"] else ""

    # Salary Breakdown
    data["basic_salary"] = re.search(r"Basic Salary\s+([\d,]+)", raw_text)
    data["basic_salary"] = data["basic_salary"].group(1) if data["basic_salary"] else ""

    data["accommodation"] = re.search(r"Accommodation\s+([\d,]+)", raw_text)
    data["accommodation"] = data["accommodation"].group(1) if data["accommodation"] else ""

    data["conveyance_allowance"] = re.search(r"Conveyance Allowance\s+([\d,]+)", raw_text)
    data["conveyance_allowance"] = data["conveyance_allowance"].group(1) if data["conveyance_allowance"] else ""

    data["special_pay"] = re.search(r"Special pay\s+([\d,]+)", raw_text)
    data["special_pay"] = data["special_pay"].group(1) if data["special_pay"] else ""

    data["medical"] = re.search(r"Medical\s+([\d,]+)", raw_text)
    data["medical"] = data["medical"].group(1) if data["medical"] else ""

    data["total_earning"] = re.search(r"Total Earning\s+([\d,]+)", raw_text)
    data["total_earning"] = data["total_earning"].group(1) if data["total_earning"] else ""

    # Deductions
    data["tax"] = re.search(r"Tax\s+([\d,]+)", raw_text)
    data["tax"] = data["tax"].group(1) if data["tax"] else ""

    data["total_deduction"] = re.search(r"Total Deduction\s+([\d,]+)", raw_text)
    data["total_deduction"] = data["total_deduction"].group(1) if data["total_deduction"] else ""

    data["net_payment"] = re.search(r"Net Payment:\s*([\d,]+)", raw_text)
    data["net_payment"] = data["net_payment"].group(1) if data["net_payment"] else ""

    return data


def autofill_missing_values(data_list):
    last_seen = {}
    for row in data_list:
        for key, value in row.items():
            if value:  # update last seen if not empty
                last_seen[key] = value
            elif key in last_seen:  # if empty, use last seen
                row[key] = last_seen[key]
    return data_list