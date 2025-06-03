
from django.shortcuts import render
from main.models import CV
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings


def main_page(request):
    cv_all_list = CV.objects.only("first_name", "last_name", "skills")
    return render(request, 'main_page.html', {"cv_all_list": cv_all_list})


def cv_details(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    return render(request, 'cv_details.html', {"cv": cv})


def cv_pdf_download(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    html_string = render_to_string('cv_details.html', {"cv": cv})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{cv.first_name}_{cv.last_name}_CV.pdf"'
    pisa_status = pisa.CreatePDF(src=html_string, dest=response)
    if pisa_status.err:
        return HttpResponse('Error', status=500)
    return response


def settings_view(request):
    return render(request, 'settings.html')


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def translate_text(text, language):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a professional translator. "
                                              f"Translate the following text to {language} "
                                              f"while preserving formatting."},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
            max_tokens=2000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Translation failed: {str(e)}")


@csrf_exempt
def translate_cv_view(request, cv_id):
    cv = CV.objects.get(id=cv_id)

    if request.method == "POST":
        language = request.POST.get("language")

        # Prepare the text to be translated
        original_text = f"""
        First Name: {cv.first_name}
        Last Name: {cv.last_name}
        Bio: {cv.bio}
        Skills: {cv.skills}
        Projects: {cv.projects}
        Contacts: {cv.contacts}
        """

        try:
            translated_text = translate_text(original_text, language)
            return render(request, "cv_translation.html", {
                "translated": translated_text,
                "cv": cv,
                "language": language
            })
        except Exception as e:
            return render(request, "cv_translation.html", {
                "error": str(e),
                "cv": cv,
                "language": language
            })

    return render(request, "cv_details.html", {"cv": cv})