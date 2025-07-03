if __name__ == "__main__":
    import sys

    sys.dont_write_bytecode = True
    from web.app import app

    app.run(debug=True)
