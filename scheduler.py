"""
Automated Scraper Scheduler
Runs scraping jobs at specified times daily using the 'schedule' library
"""

from schedule import *
from time import *
from datetime import *
from scraper import scrape_and_save

# Configuration: Define all your scraping jobs here
SCRAPE_JOBS = [
    {
        "url": "https://www.web-scraping.dev/products",
        "time": "23:30",  # 11:30 pm daily
        "name": "Web Scraping Daily Job",
        "enabled": True
    },
    {
        "url": "https://www.flipkart.com/search?q=laptop",
        "time": "14:00",  # 2 PM daily
        "name": "Flipkart Laptops Daily Job",
        "enabled": False  # Change to True to enable
    },
    {
        "url": "https://www.walmart.com/search?q=laptop",
        "time": "18:00",  # 6 PM daily
        "name": "Walmart Laptops Daily Job",
        "enabled": False  # Change to True to enable
    }
]


def job_wrapper(url, job_name):
    """
    Wrapper function to execute scraping job with error handling
    """
    try:
        print(f"\n{'='*70}")
        print(f"⏰ SCHEDULED JOB STARTED")
        print(f"📋 Job Name: {job_name}")
        print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌐 URL: {url}")
        print(f"{'='*70}\n")
        
        success, message, df, count = scrape_and_save(url)
        
        if success:
            print(f"\n✅ Job completed successfully!")
            print(f"   📊 Scraped {count} products")
            print(f"   💾 Files saved in 'scraped_data' folder\n")
        else:
            print(f"\n❌ Job failed: {message}\n")
    
    except Exception as e:
        print(f"\n❌ Unexpected error in job '{job_name}': {str(e)}\n")


def schedule_all_jobs():
    """
    Schedule all enabled jobs at specified times
    """
    print("\n" + "="*70)
    print("🤖 SCHEDULER INITIALIZATION")
    print("="*70 + "\n")
    
    scheduled_count = 0
    
    for job in SCRAPE_JOBS:
        if job["enabled"]:
            every().day.at(job["time"]).do(
                job_wrapper,
                url=job["url"],
                job_name=job["name"]
            )
            print(f"✅ Scheduled: {job['name']:<25} at {job['time']}")
            scheduled_count += 1
        else:
            print(f"⏭️  Skipped:   {job['name']:<25} (disabled)")
    
    print(f"\n{'='*70}")
    print(f"📊 Total jobs scheduled: {scheduled_count}")
    print(f"{'='*70}\n")


def run_scheduler():
    """
    Run the scheduler indefinitely
    Checks every 60 seconds if any job needs to run
    """
    schedule_all_jobs()
    
    print("🚀 Scheduler is running... (Press Ctrl+C to stop)\n")
    
    try:
        while True:
            run_pending()
            sleep(60)  # Check every 60 seconds

    except KeyboardInterrupt:
        print("\n\n🛑 Scheduler stopped by user")


# Run the scheduler
if __name__ == "__main__":
    run_scheduler()
