# -*- coding: utf-8 -*-
# Part of eagle. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    activity_date = fields.Date('Date')
    start_time = fields.Float('Starting Time')
    end_time = fields.Float('Ending Time')
    agent_name = fields.Many2one('res.company', "Agent Name")
    legend = fields.Many2one('legend.activities', "Legend Activity")


class CompanyName(models.Model):
    _inherit = "res.company"

class AgentActivities(models.Model):
    _name ="agent.activities"
    _description = "Agent Activities"
    name = fields.Char("Agent")
    description = fields.Char("Agent Activities")

class LegendActivities(models.Model):
    _name ="legend.activities"
    _description = "Legend Activities"
    name = fields.Char("Legend")
    description = fields.Char("Agent Activities")

class ActivitiesPlanning(models.Model):
    _name ="activities.planning"
    _description = "Activities Planning"
    name = fields.Many2one('res.partner', "Name")
    agent_name = fields.Many2one('res.company', "Agent Name")
    description = fields.Char("Activities Planning")