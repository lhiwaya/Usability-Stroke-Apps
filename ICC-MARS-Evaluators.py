# Learn more: https://www.statology.org/intraclass-correlation-coefficient-python/

# **ICC3**: A fixed set of :math:`k` raters rate each target. There is no
# generalization to a larger population of raters. ICC2 and ICC3 remove
# mean differences between raters, but are sensitive to interactions.
# The difference between ICC2 and ICC3 is whether raters are seen as fixed
# or random effects.

# Then, for each of these cases, the reliability can either be estimated for 
# a single rating or for the average of :math:`k` ratings. The 1 rating case 
# is equivalent to the average intercorrelation, while the :math:`k` rating 
# case is equivalent to the Spearman Brown adjusted reliability. 
# **ICC1k**, **ICC2k**, **ICC3K** reflect the means of :math:`k` raters.

import pandas as pd
import pingouin as pg

#create DataFrame
df_engagement = pd.DataFrame({'app': ['Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',],
                   'evaluator': ['Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1',
                                 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2',
                                 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3',],
                   'mean_rating': [4.0, 3.0, 3.8, 3.0, 3.0, 3.2, 3.6, 2.4, 2.8, 1.2, 2.8, 3.0, 2.0, 3.4, 2.4, 2.6,
                                   4.4, 3.2, 2.2, 3.2, 3.8, 2.8, 1.8, 3.2, 2.2, 2.6, 2.4, 4.2, 1.8, 3.6, 1.8, 2.4, 
                                   4.2, 2.0, 3.2, 3.6, 3.8, 5.0, 2.8, 4.4, 2.2, 3.4, 3.2, 4.6, 1.8, 2.8, 2.6, 4.4]})

#view first five rows of DataFrame
df_engagement.head()
print("\nEngagement - First five rows of DataFrame")
print(df_engagement.head())

icc_engagement = pg.intraclass_corr(data=df_engagement, targets='app', raters='evaluator', ratings='mean_rating')

icc_engagement.set_index('Type')
print("\nEngagement - ICC Results")
print(icc_engagement)

#create DataFrame
df_functionality = pd.DataFrame({'app': ['Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',],
                   'evaluator': ['Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1',
                                 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2',
                                 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3',],
                   'mean_rating': [5.00, 3.75, 3.50, 5.00, 4.25, 4.25, 3.00, 4.75, 4.25, 3.75, 4.50, 3.75, 3.50, 4.50, 5.00, 2.75,
                                   5.00, 4.25, 4.75, 4.75, 4.25, 3.75, 2.75, 5.00, 4.00, 4.25, 5.00, 4.00, 5.00, 3.75, 5.00, 4.75,
                                   5.00, 3.00, 5.00, 3.75, 4.75, 4.75, 2.75, 4.50, 2.75, 3.75, 4.75, 4.25, 3.75, 3.50, 4.25, 4.50]})

#view first five rows of DataFrame
df_functionality.head()
print("\nFunctionality - First five rows of DataFrame")
print(df_functionality.head())


icc_functionality = pg.intraclass_corr(data=df_functionality, targets='app', raters='evaluator', ratings='mean_rating')

icc_functionality.set_index('Type')
print("\nFunctionality - ICC Results")
print(icc_functionality)

#create DataFrame
df_aesthetic = pd.DataFrame({'app': ['Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',],
                   'evaluator': ['Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1',
                                 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2',
                                 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3',],
                   'mean_rating': [3.67, 2.67, 3.33, 2.67, 4.00, 2.33, 2.67, 3.67, 2.33, 2.33, 2.67, 2.67, 2.33, 3.33, 2.67, 2.00,
                                   3.33, 1.67, 3.33, 3.33, 3.33, 2.67, 2.67, 4.00, 3.00, 3.00, 3.67, 3.67, 3.33, 3.33, 2.33, 3.33,
                                   4.33, 2.00, 4.33, 3.67, 4.00, 3.67, 2.67, 4.00, 2.67, 3.67, 4.00, 4.00, 2.67, 3.00, 3.33, 4.00]})

#view first five rows of DataFrame
df_aesthetic.head()
print("\nAesthetic - First five rows of DataFrame")
print(df_aesthetic.head())


icc_aesthetic = pg.intraclass_corr(data=df_aesthetic, targets='app', raters='evaluator', ratings='mean_rating')

icc_aesthetic.set_index('Type')
print("\nAesthetic - ICC Results")
print(icc_aesthetic)

#create DataFrame
df_information = pd.DataFrame({'app': ['Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',],
                   'evaluator': ['Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1',
                                 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2',
                                 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3',],
                   'mean_rating': [4.14, 4.14, 4.20, 2.80, 3.66, 4.14, 3.50, 3.20, 3.40, 2.60, 3.17, 4.00, 2.60, 3.40, 3.20, 3.33,
                                   4.71, 4.00, 4.75, 3.40, 3.67, 4.43, 2.17, 4.40, 4.00, 3.40, 4.17, 4.00, 2.50, 3.67, 2.60, 3.60,
                                   4.57, 2.67, 4.60, 3.60, 4.00, 4.86, 2.17, 4.33, 3.00, 3.00, 4.14, 4.17, 1.50, 3.50, 3.80, 4.00]})

#view first five rows of DataFrame
df_information.head()
print("\nInformation - First five rows of DataFrame")
print(df_information.head())


icc_information = pg.intraclass_corr(data=df_information, targets='app', raters='evaluator', ratings='mean_rating')

icc_information.set_index('Type')
print("\nInformation - ICC Results")
print(icc_information)

#create DataFrame
df_subjective = pd.DataFrame({'app': ['Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',
                            'Constant Therapy', 'RecoverBrain Language Therapy', 'AntiCoagEvaluator', 'Rehab Coach: CVA Stroke Rehabi', 'My Aphasia Coach', 'Stroke Riskometer', 'Conversation Therapy Lite', 'ViaTherapy', 'IV Stroke Thrombolysis', 'Hope After Stroke', 'Press calc', 'MyTRCare - Stroke Recovery', 'Stroke Recovery Predictor', 'Number Therapy Lite', 'Hand exercises stroke recovery', 'Stroke Management',],
                   'evaluator': ['Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1', 'Eval 1',
                                 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2', 'Eval 2',
                                 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3', 'Eval 3',],
                   'mean_rating': [4.25, 3.50, 3.67, 2.75, 3.00, 2.75, 2.75, 3.00, 2.67, 1.00, 2.25, 3.00, 2.00, 2.50, 2.25, 1.50,
                                   4.00, 1.25, 3.25, 2.75, 3.75, 3.25, 1.25, 4.00, 2.75, 2.50, 3.50, 3.75, 1.25, 3.25, 1.00, 2.00,
                                   3.75, 1.75, 4.00, 1.75, 2.50, 5.00, 1.25, 4.00, 1.25, 2.75, 4.00, 3.50, 1.00, 2.25, 3.00, 3.75]})

#view first five rows of DataFrame
df_subjective.head()
print("\nSubjective - First five rows of DataFrame")
print(df_subjective.head())


icc_subjective = pg.intraclass_corr(data=df_subjective, targets='app', raters='evaluator', ratings='mean_rating')

icc_subjective.set_index('Type')
print("\nSubjective - ICC Results")
print(icc_subjective)