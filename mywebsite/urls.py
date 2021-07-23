from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
app_name = "backoffice"
urlpatterns = [
    path('', views.index),
    # path("", views.index, name="IndexView"),
    # path("config/", views.stripe_config),
    # path('create-checkout-session/', views.create_checkout_session),
    # path('success/', views.success),
    # path('cancel/', views.cancel),
    # path("cancel_sub_stripe/", views.cancel_sub_stripe, name="cancel_sub_stripe"),
    # path("reactivate_sub_stripe/", views.reactivate_sub_stripe, name="reactivate_sub_stripe"),
    # path("login/", views.LoginView.as_view(), name="LoginView"),
    # path("logout/", views.logout_user, name="logout_user"),
    # path("signin/", views.SignInView.as_view(), name="SignInView"),
    # path("signin/<int:account_id>/confirm_account_email/", views.confirm_account_email, name="confirm_account_email"),
    # path("campaigns/", views.CampaignsView.as_view(), name="CampaignsView"),
    # path("analytics/", views.get_all_campaigns, name="get_all_campaigns"),
    # path("analytics/<int:pk>/", views.campaign_report, name="campaign_report"),
    # path("analytics/<int:pk>/report_quest_answer_export/", views.report_quest_answer_export, name="report_quest_answer_export"),
    # path("analytics/<int:pk>/report_results_tags_export/", views.report_results_tags_export, name="report_results_tags_export"),
    # path("account/", views.AccountView.as_view(), name="AccountView"),
    # path("create_personality_quiz/", views.CreatePersonalityQuizView.as_view(), name="CreatePersonalityQuizView"),
    # path("create_training_quiz/", views.CreateTrainingQuizView.as_view(), name="CreateTrainingQuizView"),
    # path("<int:pk>/edit_personality_quiz/", views.EditPersonalityQuizView.as_view(), name="EditPersonalityQuizView"),
    # path("<int:pk>/edit_training_quiz/", views.EditTrainingQuizView.as_view(), name="EditTrainingQuizView"),
    # path("<int:pk>/preview/", views.CampaignOnlinePreviewView.as_view(), name="CampaignOnlinePreviewView"),
    # path("<int:pk>/manage_questions_excel/", views.ManageQuestionsExcel.as_view(), name="ManageQuestionsExcel"),
    # path("<int:pk>/manage_results_excel/", views.ManageResultsExcel.as_view(), name="ManageResultsExcel"),

]

if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
