from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

test_db_bp = Blueprint('test_db', __name__) # Create a Blueprint for testing the database connection

@test_db_bp.route('/test-db-1', methods=['GET'])
def test_db_1():
    try:
        return jsonify({'message': 'Database connection successful! in route 1', 'result': None}), 200
    except Exception as e:
        return jsonify({'message': 'Database connection failed! in route 1', 'error': str(e)}), 500
    
@test_db_bp.route('/test-db-2', methods=['GET'])
def test_db_2():
    try:
        return jsonify({'message': 'Database connection successful! in route 2', 'result': None}), 200
    except Exception as e:
        return jsonify({'message': 'Database connection failed! in route 2', 'error': str(e)}), 500