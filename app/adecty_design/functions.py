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


from adecty_design.properties import Font, Margin
from adecty_design.widgets import Card, Text
from app.adecty_design import colors


def message_error_get(text):
    message = Card(widgets=[
        Text(
            text=text,
            font=Font(
                size=12,
                weight=500,
                color=colors.background,
            ),
        )
    ], color_background=colors.negative, margin=Margin(down=12))
    return message
