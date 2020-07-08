from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import UserActivity,UserDetail


class UserActivityLog(View):

    def get(self, request):
        response = {'ok': False, 'members': ''}
        try:
            details_list = []
            user_details = UserDetail.objects.filter().values('id', 'name', 'time_zone')
            for details in user_details:
                user_id = details.get('id')
                details_dict = {'id': user_id, 'real_name': details.get('name'), 'tz': details.get('time_zone')}
                activity_period = []
                user_activity_obj = UserActivity.objects.filter(user_id=user_id).order_by('start_time').values('start_time', 'end_time')
                if user_activity_obj:
                    for acty in user_activity_obj:
                        activity_period.append({'start_time': str(acty['start_time']), 'end_time': str(acty['end_time'])})
                details_dict.update({'activity_periods': activity_period})

                details_list.append(details_dict)
            response.update({'ok': True, 'members': details_list})
        except Exception as e:
            response.update({'ok': False, 'members': ''})

        return JsonResponse(response)

