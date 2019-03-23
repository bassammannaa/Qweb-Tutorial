# **Q web Report - Wizard Report**

#### Introduction

This types of reports has to have **<u>2 XML files</u>** + **<u>2 Payton files</u>** in addition to add the report link in menu XML file

**<u>1- Under wizard folder:</u>**

**One XML file** : for wizard form view design.
**One Python file**: for prepare the fields that will appear in wizard form and also the required action when the suer click print the report
When you click print, the code will call the action of the report

**<u>2- Under report folder:</u>**

**One XML file</u>**: for designing the report layout
**One Python file**: for preparing the required recordset that need to appear in the report

**<u>3- menu XML files</u>**

**One menu action</u>**: to access to the wizard form
**One menu action (action disable)**: to access to form report by code so need to appear to end user



#### System main menu

<b>file path: </b> Qweb-Tutorial/wizardreport/view/menu.xml</u>

Menu action ID (app_sum_rep_wiz_wizard_menu_action) will take you to form action name (app_sum_rep_wiz_wizard_action_window)

Also there is another report action with False value which means the action is disabled, this is the report that will appear to end user, it is False action because we will call this report by python code
report model : will map to main model that will use to preview the data
name & file: will map to report id in file (report \ appsumrepview.xml)



#### Wizard report form view

<b>file path: </b>Qweb-Tutorial/wizardreport/view/appsumwizrepwiz.xml

This file should be under folder wizard
This file contains the action template that will call by system menu
And also contains the excat form veiw that will appear to end user when he click on the report.
<b>app_sum_rep_wiz</b> is model that link to this form view
This view have to contains to buttons (Print & Cancel)
Print button will call the function that in mode <b>app_sum_rep_wiz</b>


#### Wizard report model

<b>file path: </b>Qweb-Tutorial/wizardreport/view/app_sum_rep_wiz.py

This file should be under folder wizard

This model should be transit model <b>models.TransientModel></b>
Should contains all fields that will use and appear in wizard report view
Has to have function name called (print_report) to allow print another report the action name of this report is (action_report_app_sum_wiz_rep_wiz)


#### Main report design

<b>file path: </b>Qweb-Tutorial/wizardreport/report/appsumrepview.xml
This file should be under folder report
Since this report will called by python code and some data model will pass to it using code, this report need to model saved in the same report folder ()

#### Main report model

<b>file path: </b>Qweb-Tutorial/wizardreport/report/appsumrep.py

This file should be under folder report
This model should be transit model <b>models.AbstractModel></b> 
This model name should be like (report.report name)
should contains function name (_get_report_values) that will return all report recordsets

