import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Setup the Selenium WebDriver
    driver = webdriver.Chrome()

    # Assuming doctorsName, doctorsEducation, etc. are defined as empty lists
    doctorsName = []
    doctorsEducation = []
    doctorsSpeciality = []
    doctorsExperience = []
    doctorsChamber = []
    doctorsLocation = []
    doctorsConcentration = []

    # Loop through the pages to scrape data
    #Here we scrape 25 pages on each iteration Example (1-25,26-50,).
    for id in range(1, 26):  # Adjust the range as needed
        try:
            target_url = f"https://sasthyaseba.com/search?type=doctor&country_id=22&page={id}"
            driver.get(target_url)
            print(f"Navigating to: {target_url}")

            # Wait for the main page to load
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "searchAll")))
                # time.sleep(2)  # Adjust sleep time as necessary
                
                # Re-find the doctors list inside the loop
                doctors = driver.find_elements(By.CLASS_NAME, "searchAll")
                numDoctors = len(doctors)
                print(f"Found {numDoctors} doctors on the page.")

                for i in range(numDoctors):
                    # RE-FIND the doctors list every time the loop runs
                    doctors = driver.find_elements(By.CLASS_NAME, "searchAll")
                    
                    # Check for stale elements and potential out-of-bounds access
                    if i < len(doctors):
                        # link = doctors[i].find_element(By.PARTIAL_LINK_TEXT, "View all")
                        link = doctors[i].find_element(By.TAG_NAME, "a")
                        link.click()
                        
                        # time.sleep(1)  # Wait for the new page to load
                        # Wait for the new page to load
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "left")))
                        # webdriver_wait = WebDriverWait(driver, 10).until(EC.)
                        
                        # Scrape the doctor's details
                        name = driver.find_elements(By.TAG_NAME, "h1")[0].text

                        education_element = driver.find_elements(By.TAG_NAME, "h6")[0]
                        education_list = [elem.text for elem in education_element.find_elements(By.TAG_NAME, "a")]
                        education = ",".join(education_list) if education_list else "N/A"
                        speciality = driver.find_elements(By.TAG_NAME, "h6")[1].text
                        experience_text = driver.find_elements(By.TAG_NAME, "h6")[2].text.split()[0] if driver.find_elements(By.TAG_NAME, "h6")[2].text else "N/A"
                        experience = experience_text if experience_text.isnumeric() else "N/A"
                        chamber = driver.find_elements(By.TAG_NAME, "h6")[5].text 
                        split_location= driver.find_elements(By.TAG_NAME, "h6")[6].text.split(",")
                        # re_split_location = re.split(r'[, -]', split_location)  
                        # location = re_split_location[-3] if len(re_split_location) > 1 else "N/A"
                        location = split_location[-2] if len(split_location) > 1 else "N/A"
                        concentration_element = driver.find_element(By.ID, "concentrations")
                        concentration_list = [elem.text for elem in concentration_element.find_elements(By.TAG_NAME, "li")]                   
                        concentration = ",".join(concentration_list) if concentration_list else "N/A"

                        # Append the scraped data to the lists
                        doctorsName.append(name)
                        doctorsEducation.append(education)
                        doctorsSpeciality.append(speciality)
                        doctorsExperience.append(experience)
                        doctorsChamber.append(chamber)
                        doctorsLocation.append(location)
                        doctorsConcentration.append(concentration)
                        
                        print(f"Scraped details for: {name}")
                        

                        driver.back()
                        
                        # Wait for the main page to be visible again
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "searchAll")))
                        # time.sleep(1)  # Adjust sleep time as necessary
                    else:
                        print(f"Could not find doctor at index {i} after navigation.")

            except Exception as e:
                print(f"Error scraping data on page {id}: {e}")
        finally:
            print(f"Completed scraping page {id}.")

    driver.quit()
    print("\nBrowser closed.")

    #Create DataFrame from the scraped data
    df = pd.DataFrame({
        'Doctor Name': doctorsName,
        'Education': doctorsEducation,
        'Speciality': doctorsSpeciality,
        'Experience': doctorsExperience,
        'Chamber': doctorsChamber,
        'Location': doctorsLocation,
        'Concentration': doctorsConcentration,

    })

    # Save the DataFrame to a CSV file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(script_dir, "../data/raw")
    df.to_csv(f"{raw_data_dir}/doctors_raw_data(1_25).csv", index=False)



if __name__ == "__main__":
    main()

