# Build a small job application tracker using a dictionary.

# Each job should contain:
# - Company
# - Role
# - Location
# - Status
# Add at least three job records. Then:
# 1. Print all company names.
# 2. Find all jobs with status "Applied".
# 3. Update one job's status to "Interview".
# 4. Print the updated records.
job_tracker = {
    "001": {
        "Company": "Infosys",
        "Role": "Backend Developer",
        "Location": "Pune, Maharashtra",
        "Status": "Interview Scheduled",
    },
    "002": {
        "Company": "Razorpay",
        "Role": "Software Engineer",
        "Location": "Bengaluru, Karnataka",
        "Status": "Applied",
    },
    "003": {
        "Company": "Zomato",
        "Role": "Data Analyst",
        "Location": "Remote",
        "Status": "Rejected",
    },
}
# 1. Print all company names.
for key,value in job_tracker.items():
    # print(f"{value['Company']}")
    print(key ,":",value['Company'])
    
# 2. Find all jobs with status "Applied".
for key,value in job_tracker.items():
    if value["Status"]=="Applied":
        print(f"{value['Company']} ({value['Role']})")
# 3. Update one job's status to "Interview".
job_tracker["003"]['Status']='Interview'
# 4. Print the updated records.
for key,value in job_tracker.items():
    print(key,":",value)