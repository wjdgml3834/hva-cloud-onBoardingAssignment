import csv
import atexit

from flask import Flask, render_template, request, redirect, jsonify

from utilities.resource_manager import deploy_resources, delete_resource_group

from utilities.database_manager import get_connection, create_table, save_to_azure
from utilities.api_handler import fetch_api_data


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'


def fetch_and_save():
    create_table()
    image_url = fetch_api_data()
    save_to_azure(image_url)
    return jsonify({"message": "📡Successfully Loaded Dog Images", "image_url": image_url})


@app.route('/fetch_and_save', methods=['POST'])
def fetch_and_save_endpoint():
    return fetch_and_save()


@app.route('/get_dog_image', methods=['GET'])
def get_dog_image():
    # 데이터베이스에서 이미지 URL 가져오기
    image_url = get_image_url_from_database()
    return jsonify({"image_url": image_url})


def get_image_url_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    # 가장 최근에 저장된 이미지 URL 가져오기
    cursor.execute("SELECT TOP 1 ImageURL FROM dbo.DogImages ORDER BY ID DESC")
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    else:
        return None
