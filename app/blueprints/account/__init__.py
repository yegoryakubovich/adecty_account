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


from flask import Blueprint, request, redirect

from adecty_api_client.adecty_api_client_error import AdectyApiClientError
from adecty_design.properties import Font, Margin
from adecty_design.widgets import Form, InputText, Text, InputButton, View, ViewType, Button, ButtonType
from adecty_design.widgets.required import Navigation
from app.adecty_api_client import adecty_api_client
from app.adecty_design import interface
from app.adecty_design.functions import message_error_get
from app.functions.data_input import data_input


blueprint_account = Blueprint('blueprint_account', __name__, url_prefix='/account')


@blueprint_account.route('/create', endpoint='account_create', methods=('GET', 'POST'))
def account_create():
    username = ''
    password = ''

    message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            response = adecty_api_client.account.create(username=username, password=password)
            return redirect(location='/account/session/create')
        except AdectyApiClientError as e:
            message = message_error_get(text=e.txt)

    widgets = [
        message,
        Text(
            text='Sign up',
            font=Font(
                size=32,
                weight=700,
            ),
            margin=Margin(down=16),
        ),
        Form(widgets=[
            Text(
                text='Username',
                font=Font(
                    size=14,
                    weight=700,
                ),
            ),
            InputText(id='username', value=username),
            Text(
                text='Password',
                font=Font(
                    size=14,
                    weight=700,
                ),
            ),
            InputText(id='password', value=password, is_password=True),
            InputButton(text='Create account', margin=Margin(horizontal=8)),
        ]),
        View(type=ViewType.horizontal, widgets=[
            Text(
                text='Already have an account?',
                font=Font(
                    size=14,
                    weight=500,
                ),
                margin=Margin(right=8),
            ),
            Button(type=ButtonType.chip, text='Sign in', url='/account/session/create'),
        ]),
    ]
    interface_html = interface.html_get(widgets=widgets, active='', navigation=Navigation(items=[]))
    return interface_html


@blueprint_account.route('/session/create', endpoint='account_session_create', methods=('GET', 'POST'))
def account_session_create():
    username = ''
    password = ''

    message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            account_session_create_response = adecty_api_client.account.session_create(
                username=username,
                password=password,
            )
            account_session_token = account_session_create_response['token']

            if request.cookies.get('redirect_url'):
                response = redirect(location='/account/session/token/redirect')
            else:
                response = redirect(location='/account/get')
            response.set_cookie('account_session_token', value=account_session_token, max_age=60*60*24*7)
            return response
        except AdectyApiClientError as e:
            message = message_error_get(text=e.txt)

    widgets = [
        message,
        Text(
            text='Sign in',
            font=Font(
                size=32,
                weight=700,
            ),
            margin=Margin(down=16),
        ),
        Form(widgets=[
            Text(
                text='Username',
                font=Font(
                    size=14,
                    weight=700,
                ),
            ),
            InputText(id='username', value=username),
            Text(
                text='Password',
                font=Font(
                    size=14,
                    weight=700,
                ),
            ),
            InputText(id='password', value=password, is_password=True),
            InputButton(text='Sign in', margin=Margin(horizontal=8)),
        ]),
        View(type=ViewType.horizontal, widgets=[
            Text(
                text='Don`t have an account?',
                font=Font(
                    size=14,
                    weight=500,
                ),
                margin=Margin(right=8),
            ),
            Button(type=ButtonType.chip, text='Sign up', url='/account/create'),
        ]),
    ]
    interface_html = interface.html_get(widgets=widgets, active='', navigation=Navigation(items=[]))
    return interface_html


@blueprint_account.route('/session/token/get', endpoint='account_session_token_get', methods=('GET', ))
def account_session_token_get():
    redirect_url = request.args.get('redirect_url')
    if redirect_url not in ['api.adecty.com', 'pay.adecty.com']:
        return redirect(location='/')

    response = redirect(location='/account/session/token/redirect')
    response.set_cookie(key='redirect_url', value=redirect_url, max_age=60*10)

    return response


@blueprint_account.route('/session/token/redirect', endpoint='account_session_token_redirect', methods=('GET', ))
@data_input({'account_session_token': True})
def account_session_token_redirect(account_session_token):
    redirect_url = request.cookies.get('redirect_url')
    if not redirect_url:
        return redirect(location='/')

    response = redirect(
        location='https://{redirect_url}/account/session/token/save?'
                 'account_session_token={account_session_token}'.format(
            redirect_url=redirect_url,
            account_session_token=account_session_token,
        )
    )
    response.set_cookie(key='redirect_url', value='', max_age=0)
    return response


@blueprint_account.route('/get', endpoint='account_get', methods=('GET', ))
@data_input({'account_session_token': True})
def account_get(account_session_token):
    widgets = [
        Text(
            text='My account',
            font=Font(
                size=32,
                weight=700,
            ),
            margin=Margin(down=16),
        ),
    ]
    interface_html = interface.html_get(widgets=widgets, active='account_get')
    return interface_html


@blueprint_account.route('/update', endpoint='account_update', methods=('GET', ))
@data_input({'account_session_token': True})
def account_update(account_session_token):
    widgets = [
        Text(
            text='Settings',
            font=Font(
                size=32,
                weight=700,
            ),
            margin=Margin(down=16),
        ),
    ]
    interface_html = interface.html_get(widgets=widgets, active='account_update')
    return interface_html
