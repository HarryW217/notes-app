from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # Turn the above line off when running in production.