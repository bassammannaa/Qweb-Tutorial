class ApplicationSummary(models.AbstractModel):
    _name = "report.housemaid.app_sum_rep"
    _description = "Application Supmmary"


    @api.model
    def _get_report_values(self, docids, data=None):
        if data['from_date'] and data['from_date']:
            domain = [
                ('tran_date', '>=', data['from_date']),
                ('tran_date', '<=', data['to_date']),
            ]
            if data['external_office_trans']:
                domain = [
                    ('tran_date', '>=', data['from_date']),
                    ('tran_date', '<=', data['to_date']),
                    ('tran_name', '=', data['external_office_trans']),
                ]


        docs = self.env['housemaid.configuration.externalofficetrans'].search(domain)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': 'housemaid.configuration.externalofficetrans',
            'docs': docs,
        }
        return docargs
