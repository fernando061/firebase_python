from app import create_app
import sys
if __name__ == "__main__":
    config = 'development'
    if len(sys.argv) > 1:
        config = sys.argv[1]

    app = create_app(config)
    app.run(debug=True)