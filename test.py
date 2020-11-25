from app import app

if __name__ in ["__main__", "test"]:
    try:
        if __name__ == "__main__":
            app.run()

    except Exception as e:
        print(e)

