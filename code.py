import sentry_sdk

# Initialize Sentry
sentry_sdk.init(
    dsn="https://f90fdd163102a4f004eea263f2af8254@o4507498194927616.ingest.de.sentry.io/4507498206789712",  # Replace with your actual Sentry DSN
    traces_sample_rate=1.0  # Adjust the sample rate as needed
)

def main():
    try:
        # Code that raises an error
        1 / 0
    except ZeroDivisionError as e:
        # Capture the exception with Sentry
        sentry_sdk.capture_exception(e)
        print("Error captured and sent to Sentry")

if __name__ == "__main__":
    main()
