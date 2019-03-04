{
  "id": "ea05def1-f09b-4513-98f4-52c6fdde3338",
  "version": "2.0",
  "name": "login",
  "url": "https://esia-dev.test.gosuslugi.ru",
  "tests": [{
    "id": "2b68695e-6d7b-484e-aae8-cfe0cf29b262",
    "name": "1-1",
    "commands": [{
      "id": "2c24e2ef-41a6-44b8-abce-967741125b35",
      "comment": "",
      "command": "open",
      "target": "/idp/rlogin?cc=bp",
      "targets": [],
      "value": ""
    }, {
      "id": "c6c6ff45-52da-4a8a-937f-89bc688d38c8",
      "comment": "",
      "command": "setWindowSize",
      "target": "1366x728",
      "targets": [],
      "value": ""
    }, {
      "id": "4152f40f-e9bf-4323-b018-fa3ca0897e65",
      "comment": "",
      "command": "click",
      "target": "id=mobileOrEmail",
      "targets": [
        ["id=mobileOrEmail", "id"],
        ["name=mobileOrEmail", "name"],
        ["css=#mobileOrEmail", "css:finder"],
        ["xpath=//input[@id='mobileOrEmail']", "xpath:attributes"],
        ["xpath=//form[@id='authnFrm']/div/div[3]/dl/dd/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e474b934-ef58-4395-a3c8-b552231429e7",
      "comment": "",
      "command": "type",
      "target": "id=mobileOrEmail",
      "targets": [
        ["id=mobileOrEmail", "id"],
        ["name=mobileOrEmail", "name"],
        ["css=#mobileOrEmail", "css:finder"],
        ["xpath=//input[@id='mobileOrEmail']", "xpath:attributes"],
        ["xpath=//form[@id='authnFrm']/div/div[3]/dl/dd/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "89988254554"
    }, {
      "id": "63f071bf-7b21-41b2-952c-708172dc1639",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='authnFrm']/div/div[3]/dl[3]/dd/input", "xpath:idRelative"],
        ["xpath=//dl[3]/dd/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4166b339-0f9d-466e-a2f9-fe5f1d0848d3",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='authnFrm']/div/div[3]/dl[3]/dd/input", "xpath:idRelative"],
        ["xpath=//dl[3]/dd/input", "xpath:position"]
      ],
      "value": "123"
    }, {
      "id": "a12ab112-9ea7-484a-92bf-83ffa8c579f8",
      "comment": "",
      "command": "click",
      "target": "css=#loginByPwdButton > .ui-button-text",
      "targets": [
        ["css=#loginByPwdButton > .ui-button-text", "css:finder"],
        ["xpath=//button[@id='loginByPwdButton']/span", "xpath:idRelative"],
        ["xpath=//button/span", "xpath:position"],
        ["xpath=//span[contains(.,'Войти')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "59f8881f-8d5e-498b-8b1d-a63e8e2131e0",
      "comment": "",
      "command": "click",
      "target": "css=.link-logout",
      "targets": [
        ["css=.link-logout", "css:finder"],
        ["xpath=(//a[contains(@href, '')])[7]", "xpath:href"],
        ["xpath=//div[2]/div/a", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "fc80fa61-e268-462a-80d7-7219ec027002",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["2b68695e-6d7b-484e-aae8-cfe0cf29b262"]
  }],
  "urls": ["https://esia-dev.test.gosuslugi.ru/"],
  "plugins": []
}