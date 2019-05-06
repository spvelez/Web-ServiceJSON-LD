from flask import (
     Blueprint, make_response, request, jsonify
)
from werkzeug.exceptions import NotFound, BadRequest
from novela.core import database


bp = Blueprint('api', __name__)


@bp.route('/api/sujetos', methods=['GET'])
def all_users():
    query = request.args.get('query', '')    

    if not query:
        raise BadRequest('No se indico el termino a buscar')
 
    data = database.find_by_id(query)

    if data:
        data.pop('_id')

        return jsonify(data)
    else:
        raise NotFound('No se encontró el termino ' + query)

@bp.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': e.description}), 404)


@bp.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({'error': e.description}), 400)
