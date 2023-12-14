# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:04:32 2023

@author: jmeluso
"""


def get_variables_all():

    allVars = [
        'project_artifact',
        'project_useCase',
        'credit_freqFromProjects',
        'credit_freqForTasks',
        'credit_medium',
        'satis_medium',
        'freq_seenBy2',
        'freq_seenBy1',
        'freq_seenBy0',
        'satis_taskFreq',
        'credit_importance',
        'text_whatDidWork',
        'text_whatDidntWork',
        'text_anythingElse'
    ]

    return allVars


def get_variables_categorical():

    catVars = [
        'project_artifact',
        'project_useCase',
        'credit_medium',
        ]

    return catVars


def get_variables_text():

    textVars = [
        'text_whatDidWork',
        'text_whatDidntWork',
        'text_anythingElse'
    ]

    return textVars


def get_variables_numeric():

    numericVars = [
        'credit_freqFromProjects',
        'credit_freqForTasks',
        'satis_medium',
        'freq_seenBy2',
        'freq_seenBy1',
        'freq_seenBy0',
        'satis_taskFreq',
        'credit_importance'
    ]

    return numericVars


def get_variables():

    variables = {
        'Q3': {
            'name': 'project_artifact',
            'dtype': str,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice'},
        'Q3_7': {
            'name': 'project_artifact_7',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Hardware'},
        'Q3_8': {
            'name': 'project_artifact_8',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Operating systems'},
        'Q3_9': {
            'name': 'project_artifact_9',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Languages'},
        'Q3_10': {
            'name': 'project_artifact_10',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Frameworks'},
        'Q3_17': {
            'name': 'project_artifact_17',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Libraries'},
        'Q3_11': {
            'name': 'project_artifact_11',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Packages'},
        'Q3_12': {
            'name': 'project_artifact_12',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Applications'},
        'Q3_13': {
            'name': 'project_artifact_13',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Data science'},
        'Q3_14': {
            'name': 'project_artifact_14',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Scripts'},
        'Q3_15': {
            'name': 'project_artifact_15',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Web-related'},
        'Q3_16': {
            'name': 'project_artifact_16',
            'dtype': int,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Selected Choice - Something else'},
        'Q3_16_TEXT': {
            'name': 'project_artifact_text',
            'dtype': str,
            'question': 'The following categories describe things that projects either create or work on. Which categories apply to the projects you worked on? Select all that apply. - Something else - Text'},
        'Q4': {
            'name': 'project_useCase',
            'dtype': str,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice'},
        'Q4_4': {
            'name': 'project_useCase_4',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Browsers'},
        'Q4_5': {
            'name': 'project_useCase_5',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Business & productivity applications'},
        'Q4_6': {
            'name': 'project_useCase_6',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Communication technologies'},
        'Q4_7': {
            'name': 'project_useCase_7',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Content management'},
        'Q4_14': {
            'name': 'project_useCase_14',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Education'},
        'Q4_8': {
            'name': 'project_useCase_8',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Entertainment'},
        'Q4_9': {
            'name': 'project_useCase_9',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Manufacturing'},
        'Q4_10': {
            'name': 'project_useCase_10',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Publishing'},
        'Q4_11': {
            'name': 'project_useCase_11',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Scientific research'},
        'Q4_12': {
            'name': 'project_useCase_12',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Software infrastructure'},
        'Q4_13': {
            'name': 'project_useCase_13',
            'dtype': int,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Selected Choice - Something else'},
        'Q4_13_TEXT': {
            'name': 'project_useCase_text',
            'dtype': str,
            'question': 'Projects create for different use cases. Which cases apply to the projects you worked on? Select all that apply. - Something else - Text'},
        'Q7': {
            'name': 'credit_freqFromProjects',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks?'},
        'Q7_1': {
            'name': 'credit_freqFromProjects_1',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks? - 1 - None of them'},
        'Q7_2': {
            'name': 'credit_freqFromProjects_2',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks? - 2 - Few of them'},
        'Q7_3': {
            'name': 'credit_freqFromProjects_3',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks? - 3 - Some of them'},
        'Q7_4': {
            'name': 'credit_freqFromProjects_4',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks? - 4 - Most of them'},
        'Q7_5': {
            'name': 'credit_freqFromProjects_5',
            'dtype': int,
            'question': 'In the past two years, from how many projects did you receive credit for your tasks? - 5 - All of them'},
        'Q7_6': {
            'name': 'credit_freqFromProjects_6',
            'dtype': int,
            'question': "In the past two years, from how many projects did you receive credit for your tasks? - I'm not sure"},
        'Q8': {
            'name': 'credit_freqForTasks',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit?'},
        'Q8_1': {
            'name': 'credit_freqForTasks_1',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - 1 - None of them'},
        'Q8_2': {
            'name': 'credit_freqForTasks_2',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - 2 - Few of them'},
        'Q8_3': {
            'name': 'credit_freqForTasks_3',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - 3 - Some of them'},
        'Q8_4': {
            'name': 'credit_freqForTasks_4',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - 4 - Most of them'},
        'Q8_5': {
            'name': 'credit_freqForTasks_5',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - 5 - All of them'},
        'Q8_6': {
            'name': 'credit_freqForTasks_6',
            'dtype': int,
            'question': 'In the past two years, for how many of your tasks did you receive credit? - I’m not sure'},
        'Q9': {
            'name': 'credit_medium',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice'},
        'Q9_1': {
            'name': 'credit_medium_1',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Automated metrics (e.g. GitHub Contributors)'},
        'Q9_2': {
            'name': 'credit_medium_2',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Project membership (e.g. GitHub Organizations)'},
        'Q9_3': {
            'name': 'credit_medium_3',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Project documentation (e.g. acknowledgements lists, release notes)'},
        'Q9_4': {
            'name': 'credit_medium_4',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Standardized tools (e.g. All Contributors, CRediT)'},
        'Q9_5': {
            'name': 'credit_medium_5',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Social media (e.g. Twitter, Facebook)'},
        'Q9_6': {
            'name': 'credit_medium_6',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Blogs (e.g. Medium, personal websites)'},
        'Q9_7': {
            'name': 'credit_medium_7',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Presentations (e.g. talks, conferences)'},
        'Q9_8': {
            'name': 'credit_medium_8',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - Something else'},
        'Q9_9': {
            'name': 'credit_medium_9',
            'dtype': int,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Selected Choice - I’m not sure'},
        'Q9_8_TEXT': {
            'name': 'credit_medium_text',
            'dtype': str,
            'question': 'Projects give people credit for tasks through different mediums. Through what mediums did you receive credit? Select all that apply. - Something else - Text'},
        'Q10': {
            'name': 'satis_medium',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit?'},
        'Q10_1': {
            'name': 'satis_medium_1',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit? - 1 - Extremely dissatisfied'},
        'Q10_2': {
            'name': 'satis_medium_2',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit? - 2 - Dissatisfied'},
        'Q10_3': {
            'name': 'satis_medium_3',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit? - 3 - Neither satisfied nor dissatisfied'},
        'Q10_4': {
            'name': 'satis_medium_4',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit? - 4 - Satisfied'},
        'Q10_5': {
            'name': 'satis_medium_5',
            'dtype': int,
            'question': 'How satisfied are you with the mediums through which you received credit? - 5 - Extremely satisfied'},
        'Q11': {
            'name': 'freq_seenBy2',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks?'},
        'Q11_17': {
            'name': 'freq_seenBy2_17',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks? - 1 - Never'},
        'Q11_18': {
            'name': 'freq_seenBy2_18',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks? - 2 - Rarely'},
        'Q11_19': {
            'name': 'freq_seenBy2_19',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks? - 3 - Sometimes'},
        'Q11_20': {
            'name': 'freq_seenBy2_20',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks? - 4 - Often'},
        'Q11_21': {
            'name': 'freq_seenBy2_21',
            'dtype': int,
            'question': 'How often did 2 or more people know that you performed those tasks? - 5 - Always'},
        'Q11_6': {
            'name': 'freq_seenBy2_6',
            'dtype': int,
            'question': "How often did 2 or more people know that you performed those tasks? - I'm not sure"},
        'Q12': {
            'name': 'freq_seenBy1',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks?'},
        'Q12_1': {
            'name': 'freq_seenBy1_1',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks? - 1 - Never'},
        'Q12_2': {
            'name': 'freq_seenBy1_2',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks? - 2 - Rarely'},
        'Q12_3': {
            'name': 'freq_seenBy1_3',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks? - 3 - Sometimes'},
        'Q12_4': {
            'name': 'freq_seenBy1_4',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks? - 4 - Often'},
        'Q12_5': {
            'name': 'freq_seenBy1_5',
            'dtype': int,
            'question': 'How often did 1 other person know that you performed those tasks? - 5 - Always'},
        'Q12_6': {
            'name': 'freq_seenBy1_6',
            'dtype': int,
            'question': "How often did 1 other person know that you performed those tasks? - I'm not sure"},
        'Q13': {
            'name': 'freq_seenBy0',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks?'},
        'Q13_1': {
            'name': 'freq_seenBy0_1',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks? - 1 - Never'},
        'Q13_2': {
            'name': 'freq_seenBy0_2',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks? - 2 - Rarely'},
        'Q13_3': {
            'name': 'freq_seenBy0_3',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks? - 3 - Sometimes'},
        'Q13_4': {
            'name': 'freq_seenBy0_4',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks? - 4 - Often'},
        'Q13_5': {
            'name': 'freq_seenBy0_5',
            'dtype': int,
            'question': 'How often did nobody else know that you performed those tasks? - 5 - Always'},
        'Q13_6': {
            'name': 'freq_seenBy0_6',
            'dtype': int,
            'question': "How often did nobody else know that you performed those tasks? - I'm not sure"},
        'Q14': {
            'name': 'satis_taskFreq',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit?'},
        'Q14_1': {
            'name': 'satis_taskFreq_1',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit? - 1 - Extremely dissatisfied'},
        'Q14_2': {
            'name': 'satis_taskFreq_2',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit? - 2 - Dissatisfied'},
        'Q14_3': {
            'name': 'satis_taskFreq_3',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit? - 3 - Neither satisfied nor dissatisfied'},
        'Q14_4': {
            'name': 'satis_taskFreq_4',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit? - 4 - Satisfied'},
        'Q14_5': {
            'name': 'satis_taskFreq_5',
            'dtype': int,
            'question': 'How satisfied are you with how many of your tasks received credit? - 5 - Extremely satisfied'},
        'Q15': {
            'name': 'credit_importance',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do?'},
        'Q15_28': {
            'name': 'credit_importance_28',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do? - 1 - Not at all important'},
        'Q15_29': {
            'name': 'credit_importance_29',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do? - 2 - Slightly important'},
        'Q15_30': {
            'name': 'credit_importance_30',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do? - 3 - Moderately important'},
        'Q15_31': {
            'name': 'credit_importance_31',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do? - 4 - Very important'},
        'Q15_32': {
            'name': 'credit_importance_32',
            'dtype': int,
            'question': 'How important is it to you to receive credit for the tasks you do? - 5 - Extremely important'},
        'Q16': {
            'name': 'text_whatDidWork',
            'dtype': str,
            'question': 'Think about how the projects you worked on gave people credit. From your perspective, what worked well about how they gave people credit?'},
        'Q17': {
            'name': 'text_whatDidntWork',
            'dtype': str,
            'question': 'What did not work well about how they gave people credit?'},
        'Q18': {
            'name': 'text_anythingElse',
            'dtype': str,
            'question': 'Is there anything else that you’d like to share with us?'},
        'Path1-LaborVisibility_DO': {
            'name': 'order',
            'dtype': str,
            'question': ''},
        'Path1-LaborVisibility_DO_Q28': {
            'name': 'order_Q28',
            'dtype': int,
            'question': 'Path 1 - Labor Visibility - Display Order - Q28'},
        'Path1-LaborVisibility_DO_Q13': {
            'name': 'order_Q13',
            'dtype': int,
            'question': 'Path 1 - Labor Visibility - Display Order - Q13'},
        'Path1-LaborVisibility_DO_Q12': {
            'name': 'order_Q12',
            'dtype': int,
            'question': 'Path 1 - Labor Visibility - Display Order - Q12'},
        'Path1-LaborVisibility_DO_Q11': {
            'name': 'order_Q11',
            'dtype': int,
            'question': 'Path 1 - Labor Visibility - Display Order - Q11'}
    }
    return variables


def get_variable_dtypes():
    variables = get_variables()
    dtypes = {key: variables[key]['dtype'] for key in variables.keys()}
    return dtypes


def get_variable_names():
    variables = get_variables()
    names = {key: variables[key]['name'] for key in variables.keys()}
    return names


def get_variable_questions():
    variables = get_variables()
    questions = {key: variables[key]['question'] for key in variables.keys()}
    return questions


def get_question_groups():

    questionGroups = {
        'project_artifact': [
            'project_artifact_7',
            'project_artifact_8',
            'project_artifact_9',
            'project_artifact_10',
            'project_artifact_17',
            'project_artifact_11',
            'project_artifact_12',
            'project_artifact_13',
            'project_artifact_14',
            'project_artifact_15',
            'project_artifact_16'
        ],
        'project_useCase': [
            'project_useCase_4',
            'project_useCase_5',
            'project_useCase_6',
            'project_useCase_7',
            'project_useCase_14',
            'project_useCase_8',
            'project_useCase_9',
            'project_useCase_10',
            'project_useCase_11',
            'project_useCase_12',
            'project_useCase_13'
        ],
        'credit_medium': [
            'credit_medium_1',
            'credit_medium_2',
            'credit_medium_3',
            'credit_medium_4',
            'credit_medium_5',
            'credit_medium_6',
            'credit_medium_7',
            'credit_medium_8',
            'credit_medium_9'
        ],
        'credit_freqFromProjects': [
            'credit_freqFromProjects_1',
            'credit_freqFromProjects_2',
            'credit_freqFromProjects_3',
            'credit_freqFromProjects_4',
            'credit_freqFromProjects_5',
            'credit_freqFromProjects_6'
        ],
        'credit_freqForTasks': [
            'credit_freqForTasks_1',
            'credit_freqForTasks_2',
            'credit_freqForTasks_3',
            'credit_freqForTasks_4',
            'credit_freqForTasks_5',
            'credit_freqForTasks_6'
        ],
        'satis_medium': [
            'satis_medium_1',
            'satis_medium_2',
            'satis_medium_3',
            'satis_medium_4',
            'satis_medium_5'
        ],
        'freq_seenBy2': [
            'freq_seenBy2_17',
            'freq_seenBy2_18',
            'freq_seenBy2_19',
            'freq_seenBy2_20',
            'freq_seenBy2_21',
            'freq_seenBy2_6'
        ],
        'freq_seenBy1': [
            'freq_seenBy1_1',
            'freq_seenBy1_2',
            'freq_seenBy1_3',
            'freq_seenBy1_4',
            'freq_seenBy1_5',
            'freq_seenBy1_6'
        ],
        'freq_seenBy0': [
            'freq_seenBy0_1',
            'freq_seenBy0_2',
            'freq_seenBy0_3',
            'freq_seenBy0_4',
            'freq_seenBy0_5',
            'freq_seenBy0_6'
        ],
        'satis_taskFreq': [
            'satis_taskFreq_1',
            'satis_taskFreq_2',
            'satis_taskFreq_3',
            'satis_taskFreq_4',
            'satis_taskFreq_5'
        ],
        'credit_importance': [
            'credit_importance_28',
            'credit_importance_29',
            'credit_importance_30',
            'credit_importance_31',
            'credit_importance_32'
        ]
    }

    return questionGroups


def get_option_definitions():

    optionDefinitions = {
        'project_artifact': 'Artifacts worked on',
        'project_useCase': 'Use cases of projects',
        'credit_medium': 'Credit medium',
        'credit_freqFromProjects': 'Credit from projects, frequency',
        'credit_freqForTasks': 'Credit for tasks, frequency',
        'satis_medium': 'Satisfaction with credit medium',
        'freq_seenBy2': 'Seen by 2 or more people',
        'freq_seenBy1': 'Seen by 1 other person',
        'freq_seenBy0': 'Seen by 0 other people',
        'satis_taskFreq': 'Satisfaction with credit frequency',
        'credit_importance': 'Importance of receiving credit',
        'order': 'Anchored to Invisibility (0, 1, $\geq$2 people)',
        'project_artifact_7': 'Hardware',
        'project_artifact_8': 'Operating systems',
        'project_artifact_9': 'Languages',
        'project_artifact_10': 'Frameworks',
        'project_artifact_17': 'Libraries',
        'project_artifact_11': 'Packages',
        'project_artifact_12': 'Applications',
        'project_artifact_13': 'Data science',
        'project_artifact_14': 'Scripts',
        'project_artifact_15': 'Web-related',
        'project_artifact_16': 'Something else',
        'project_useCase_4': 'Browsers',
        'project_useCase_5': 'Bus. & productivity applic.',
        'project_useCase_6': 'Communication technologies',
        'project_useCase_7': 'Content management',
        'project_useCase_14': 'Education',
        'project_useCase_8': 'Entertainment',
        'project_useCase_9': 'Manufacturing',
        'project_useCase_10': 'Publishing',
        'project_useCase_11': 'Scientific research',
        'project_useCase_12': 'Software infrastructure',
        'project_useCase_13': 'Something else',
        'credit_medium_1': 'Automated metrics (e.g. GitHub Contributors)',
        'credit_medium_2': 'Project membership (e.g. GitHub Organizations)',
        'credit_medium_3': 'Project documentation (e.g. acknowledgements lists, release notes)',
        'credit_medium_4': 'Standardized tools (e.g. All Contributors, CRediT)',
        'credit_medium_5': 'Social media (e.g. Twitter, Facebook)',
        'credit_medium_6': 'Blogs (e.g. Medium, personal websites)',
        'credit_medium_7': 'Presentations (e.g. talks, conferences)',
        'credit_medium_8': 'Something else',
        'credit_medium_9': "I'm not sure",
        'credit_freqFromProjects_1': 'None of them - 1',
        'credit_freqFromProjects_2': 'Few of them - 2',
        'credit_freqFromProjects_3': 'Some of them - 3',
        'credit_freqFromProjects_4': 'Most of them - 4',
        'credit_freqFromProjects_5': 'All of them - 5',
        'credit_freqFromProjects_6': "I'm not sure",
        'credit_freqForTasks_1': 'None of them - 1',
        'credit_freqForTasks_2': 'Few of them - 2',
        'credit_freqForTasks_3': 'Some of them - 3',
        'credit_freqForTasks_4': 'Most of them - 4',
        'credit_freqForTasks_5': 'All of them - 5',
        'credit_freqForTasks_6': "I'm not sure",
        'satis_medium_1': 'Extremely dissatisfied - 1',
        'satis_medium_2': 'Dissatisfied - 2',
        'satis_medium_3': 'Neither sat. nor dissat. - 3',
        'satis_medium_4': 'Satisfied - 4',
        'satis_medium_5': 'Extremely satisfied - 5',
        'freq_seenBy2_17': '1 - Never',
        'freq_seenBy2_18': '2 - Rarely',
        'freq_seenBy2_19': '3 - Sometimes',
        'freq_seenBy2_20': '4 - Often',
        'freq_seenBy2_21': '5 - Always',
        'freq_seenBy2_6': "I'm not sure",
        'freq_seenBy1_1': '1 - Never',
        'freq_seenBy1_2': '2 - Rarely',
        'freq_seenBy1_3': '3 - Sometimes',
        'freq_seenBy1_4': '4 - Often',
        'freq_seenBy1_5': '5 - Always',
        'freq_seenBy1_6': "I'm not sure",
        'freq_seenBy0_1': '1 - Never',
        'freq_seenBy0_2': '2 - Rarely',
        'freq_seenBy0_3': '3 - Sometimes',
        'freq_seenBy0_4': '4 - Often',
        'freq_seenBy0_5': '5 - Always',
        'freq_seenBy0_6': "I'm not sure",
        'satis_taskFreq_1': 'Extremely dissatisfied - 1',
        'satis_taskFreq_2': 'Dissatisfied - 2',
        'satis_taskFreq_3': 'Neither sat. nor dissat. - 3',
        'satis_taskFreq_4': 'Satisfied - 4',
        'satis_taskFreq_5': 'Extremely satisfied - 5',
        'credit_importance_28': 'Not at all important - 1',
        'credit_importance_29': 'Slightly important - 2',
        'credit_importance_30': 'Moderately important - 3',
        'credit_importance_31': 'Very important - 4',
        'credit_importance_32': 'Extremely important - 5',
        'order_Q28': 'Path 1 - Labor Visibility - Display Order - Q28',
        'order_Q13': 'Path 1 - Labor Visibility - Display Order - Q13',
        'order_Q12': 'Path 1 - Labor Visibility - Display Order - Q12',
        'order_Q11': 'Path 1 - Labor Visibility - Display Order - Q11'
    }
    return optionDefinitions
    
    
