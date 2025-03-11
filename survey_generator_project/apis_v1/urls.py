from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .viewsets import AnswerViewSet, ChoiceViewSet, SurveyViewSet, SectionViewSet, QuestionGroupViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='surveys')
# /surveys
# /surveys/{pk}
survey_router = NestedSimpleRouter(router, r'surveys', lookup='surveys')
survey_router.register(r'sections', SectionViewSet, basename='sections')
# /surveys/{surveyId}/sections
# /surveys/{surveyId}/sections/{sectionId}
section_router = NestedSimpleRouter(survey_router, r'sections', lookup='sections')
section_router.register(r'groups', QuestionGroupViewSet, basename='groups')
# /surveys/{surveyId}/sections/{sectionId}/groups
# /surveys/{surveyId}/sections/{sectionId}/groups/{groupId}
group_router = NestedSimpleRouter(section_router, r'groups', lookup='groups')
group_router.register(r'questions', QuestionViewSet, basename='questions')
# /surveys/{surveyId}/sections/{sectionId}/groups/{groupId}/questions
# /surveys/{surveyId}/sections/{sectionId}/groups/{groupId}/questions/{questionId}
question_router = NestedSimpleRouter(group_router, r'questions', lookup='questions')
question_router.register(r'answers', AnswerViewSet, basename='answers')
# /surveys/{surveyId}/sections/{sectionId}/groups/{groupId}/questions/{questionId}/answers
# /surveys/{surveyId}/sections/{sectionId}/groups/{groupId}/questions/{questionId}/answers/{answerId}
answer_router = NestedSimpleRouter(question_router, r'answers', lookup='answers')
answer_router.register(r'choices', ChoiceViewSet, basename='choices')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(survey_router.urls)),
    path(r'', include(section_router.urls)),
    path(r'', include(group_router.urls)),
    path(r'', include(question_router.urls)),
    path(r'', include(answer_router.urls)),
]