# -*- coding: utf-8 -*-
###################################################################################
#
#    Cybernetics Plus Co., Ltd.
#    View Password at Login and Signup Page
#
###################################################################################

{
    "name": "View Password at Login and Signup Page",
    "version": "15.0.1.0.1",
    "summary": """ 
            View Password at Login and Signup Page
            .""",
    "description": """ 
            View Password at Login and Signup Page
            .""",
    "author": "Cybernetics Plus",
    "company": "Cybernetics Plus Co., Ltd.",
    "maintainer": "Cybernetics Plus Co., Ltd.",
    "website": "https://www.cybernetics.plus",
    "live_test_url": "https://www.cybernetics.plus",
    "images": ["static/description/banner.png"],
    "category": "Website",
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
    "contributors": [
        "C+ Developer <dev@cybernetics.plus>",
    ],
  "data": ["views/auth_signup_login.xml"],
  "assets": {
      "web.assets_frontend": [
          "ctp_show_password/static/src/css/show_password.css",
          "ctp_show_password/static/src/js/show_password.js",
      ],
  },
  "pre_init_hook": "pre_init_check",
}
