def get_approval(job, score):
    print("\n==============================")
    print(f"Job Title : {job['title']}")
    print(f"Company   : {job['company']}")
    print(f"Platform  : {job['platform']}")
    print(f"Match     : {score}%")
    return input("Apply? (Y/N): ").lower() == "y"
