from otree.api import *
import csv
import logging

c = Currency
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1
    num_of_tables = 50
    comprehension_question_bonus = 0.10
    max_consecutive_timeout_pages = 2

    with open('tables.csv', encoding='utf-8-sig') as table_file:
        tables = list(csv.DictReader(table_file))


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random
    logging.info("Creating intro session")

    # Initializing participant's fields
    for player in subsession.get_players():
        player.participant.force_end = False
        player.participant.is_dropout = False
        player.participant.has_reached_main = False

    # Get 50 randomly selected tables for the practice real effort round
    random_tables = random.sample(Constants.tables, Constants.num_of_tables)
    tables = list()
    for table in random_tables:
        tables.append(table['table'])
    subsession.session.vars['tables_intro'] = tables
    answers = list()
    for table in random_tables:
        answers.append(int(table['zeros']))
    subsession.session.vars['answers_intro'] = answers


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    table_0 = models.IntegerField()
    table_1 = models.IntegerField()
    table_2 = models.IntegerField()
    table_3 = models.IntegerField()
    table_4 = models.IntegerField()
    table_5 = models.IntegerField()
    table_6 = models.IntegerField()
    table_7 = models.IntegerField()
    table_8 = models.IntegerField()
    table_9 = models.IntegerField()
    table_10 = models.IntegerField()
    table_11 = models.IntegerField()
    table_12 = models.IntegerField()
    table_13 = models.IntegerField()
    table_14 = models.IntegerField()
    table_15 = models.IntegerField()
    table_16 = models.IntegerField()
    table_17 = models.IntegerField()
    table_18 = models.IntegerField()
    table_19 = models.IntegerField()
    table_20 = models.IntegerField()
    table_21 = models.IntegerField()
    table_22 = models.IntegerField()
    table_23 = models.IntegerField()
    table_24 = models.IntegerField()
    table_25 = models.IntegerField()
    table_26 = models.IntegerField()
    table_27 = models.IntegerField()
    table_28 = models.IntegerField()
    table_29 = models.IntegerField()
    table_30 = models.IntegerField()
    table_31 = models.IntegerField()
    table_32 = models.IntegerField()
    table_33 = models.IntegerField()
    table_34 = models.IntegerField()
    table_35 = models.IntegerField()
    table_36 = models.IntegerField()
    table_37 = models.IntegerField()
    table_38 = models.IntegerField()
    table_39 = models.IntegerField()
    table_40 = models.IntegerField()
    table_41 = models.IntegerField()
    table_42 = models.IntegerField()
    table_43 = models.IntegerField()
    table_44 = models.IntegerField()
    table_45 = models.IntegerField()
    table_46 = models.IntegerField()
    table_47 = models.IntegerField()
    table_48 = models.IntegerField()
    table_49 = models.IntegerField()
    correct_counter = models.IntegerField()
    incorrect_counter = models.IntegerField()
    number_of_consecutive_timeout_pages = models.IntegerField(initial=0)

    # TODO: Review the comprehension questions
    question_payrate = models.IntegerField(
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelect
    )
    question_contribution = models.IntegerField(
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelect
    )
    question_switching_1 = models.IntegerField(
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelect
    )
    question_switching_2 = models.IntegerField(
        choices=[1, 2, 3, 4],
        widget=widgets.RadioSelect
    )

    def get_practice_round_results(self):
        submitted_answers = [self.table_0, self.table_1, self.table_2, self.table_3, self.table_4, self.table_5,
                             self.table_6, self.table_7, self.table_8, self.table_9, self.table_10, self.table_11,
                             self.table_12, self.table_13, self.table_14, self.table_15, self.table_16, self.table_17,
                             self.table_18, self.table_19, self.table_20, self.table_21, self.table_22, self.table_23,
                             self.table_24, self.table_25, self.table_26, self.table_27, self.table_28, self.table_29,
                             self.table_30, self.table_31, self.table_32, self.table_33, self.table_34, self.table_35,
                             self.table_36, self.table_37, self.table_38, self.table_39, self.table_40, self.table_41,
                             self.table_42, self.table_43, self.table_44, self.table_45, self.table_46, self.table_47,
                             self.table_48, self.table_49
                             ]
        self.correct_counter = 0
        self.incorrect_counter = 0
        for i in range(len(self.session.vars['answers_intro'])):
            if submitted_answers[i] == self.session.vars['answers_intro'][i]:
                self.correct_counter += 1
            else:
                self.incorrect_counter += 1

    def check_comprehension_questions(self, questions, answers):
        for i in range(len(questions)):
            if questions[i] == answers[i]:
                self.payoff += cu(Constants.comprehension_question_bonus)


def dropout_handler_before_next_page(player, timeout_happened):
    participant = player.participant
    if timeout_happened:
        player.number_of_consecutive_timeout_pages += 1
    else:
        player.number_of_consecutive_timeout_pages = 0
    if player.number_of_consecutive_timeout_pages >= Constants.max_consecutive_timeout_pages:
        participant.is_dropout = True


def dropout_handler_app_after_this_page(player, upcoming_apps):
    if player.participant.is_dropout:
        return upcoming_apps[-1]
    else:
        pass


# PAGES
class Introduction(Page):
    pass


page_sequence = [Introduction]

