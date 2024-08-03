from openai import OpenAI
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Professor

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
@csrf_exempt

def ask_bot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query', '')

            # Determine if the query is related to professors
            professor_related_keywords = ['professor', 'research', 'publication', 'teaching']
            is_professor_related = any(keyword in query.lower() for keyword in professor_related_keywords)

            # Default system message
            system_message = {"role": "system", "content": "You are a helpful assistant."}

            if is_professor_related:
                # Fetch professor data
                professors = Professor.objects.all()

                if not professors:
                    return JsonResponse({"error": "No professors found in the database."}, status=404)

                professor_info = "\n".join([
                    f"{prof.name}: Research Area: {prof.research_area}, Publications: {prof.publications}, Education: {prof.education}, Teaching Area: {prof.teaching_area}"
                    for prof in professors
                ])
                system_message = {"role": "system", "content": f"Professors and their details:\n{professor_info}"}

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    system_message,
                    {"role": "user", "content": query},
                ]
            )

            answer = response.choices[0].message.content
            
            return JsonResponse({"answer": answer.strip()})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)

def get_professors(request):
    if request.method == 'GET':
        try:
            professors = Professor.objects.all()
            data = [
                {
                    "name": prof.name,
                    "research_area": prof.research_area,
                    "publications": prof.publications,
                    "education": prof.education,
                    "teaching_area": prof.teaching_area
                }
                for prof in professors
            ]
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)