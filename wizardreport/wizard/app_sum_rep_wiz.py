class AppSumWizRepWiz(models.TransientModel):
    _name = "housemaid.wizard.app_sum_rep_wiz"
    _description = "Applications Summary Wizard Report"

    from_date = fields.Date(string="From Date",)
    to_date = fields.Date(string="To Date",)
    external_office_trans = fields.Many2one(comodel_name="housemaid.configuration.externalofficetransdet",
                                   string="External Office Transactions", required=False, )

    app_state = fields.Selection(app_stages, string='Application Status',)

    @api.multi
    def print_report(self):
        data = {}
        data['from_date'] = self.from_date
        data['to_date'] = self.to_date
        data['external_office_trans'] = self.external_office_trans.name

        report = self.env.ref(
            'housemaid.action_report_app_sum_wiz_rep_wiz')
        return report.report_action(self, data=data)
