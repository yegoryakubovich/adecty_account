#
# (c) 2023, Yegor Yakubovich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from flask import Blueprint, redirect
from werkzeug.exceptions import InternalServerError


blueprint_errors = Blueprint('blueprint_errors', __name__)


@blueprint_errors.app_errorhandler(404)
def errors_404(error: InternalServerError):
    return 'Not found', 404


@blueprint_errors.app_errorhandler(401)
def errors_401(error: InternalServerError):
    return redirect('/account/session/create')
