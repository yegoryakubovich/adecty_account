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


from adecty_design import Interface
from adecty_design.properties import Font
from adecty_design.widgets.icon import Icon
from adecty_design.widgets.required import Navigation, Header, Footer, NavigationItem
from app.adecty_design.colors import colors


interface = Interface(
    logo=Icon(path='app/icons/logo.svg'),
    logo_mini=Icon(path='app/icons/logo_mini.svg'),
    name='Adecty Account',
    colors=colors,
    font=Font(
        css='\'Montserrat\', sans-serif',
        html_init='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">',
        css_init="@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');",
    ),
    rounding=4,
    navigation=Navigation(
        items=[
            NavigationItem(
                id='account_get',
                name='My account',
                url='/account/get',
                icon=Icon(path='app/icons/logo_mini.svg')
            ),
            NavigationItem(
                id='account_update',
                name='Settings',
                url='/account/update',
                icon=Icon(path='app/icons/settings.svg')
            ),
        ]
    ),
    header=Header(
        navigation_items=[],
    ),
    footer=Footer(),
)
