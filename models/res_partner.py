# -*- coding: utf-8 -*-
# Part of eagle. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    activity_date = fields.Date('Date')
    start_time = fields.Float('Starting Time')
    end_time = fields.Float('Ending Time')
    agent_name = fields.Many2one('res.company', "Agent Name")
    legend = fields.Many2one('activities.legendactivity', "Activity")
    activities_ids = fields.One2many("activities.agent", 'stuff_id', "Stuff ID")

class CompanyName(models.Model):
    _inherit = "res.company"

class AgentActivities(models.Model):
    _name ="activities.agent"
    _description = "Agent Activities"
    name = fields.Char("Agent")
    description = fields.Char("Agent Activities")
    stuff_id = fields.Many2one('res.partner', "Stuff")
    agent_name = fields.Many2one('res.company', "Agent")
    legend = fields.Many2one('activities.legendactivity', "Activity")
    activity_date = fields.Date('Date')
    start_time = fields.Float('Starting Time')
    end_time = fields.Float('Ending Time')


class LegendActivities(models.Model):
    _name ="activities.legendactivity"
    _description = "Activities Legend Activities"
    name = fields.Char("Legend Activity")
    description = fields.Char("Legend Activities")

class ActivitiesPlanning(models.Model):
    _name ="activities.planning"
    _description = "Activities Planning"
    name = fields.Many2one('res.partner', "Name")
    agent_name = fields.Many2one('res.partner', "Agent Name")
    description = fields.Char("Activities Planning")