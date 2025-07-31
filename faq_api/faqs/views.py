from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from django.utils.html import strip_tags  # <-- Import this
from googletrans import Translator
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            return Response(cached_faqs)

        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        data = serializer.data

        if lang != 'en':
            translator = Translator()
            translated_data = []
            for item in data:
                try:
                    # Strip HTML tags from the answer before translating
                    answer_text = strip_tags(item['answer'])

                    translated_question = translator.translate(item['question'], dest=lang).text
                    translated_answer = translator.translate(answer_text, dest=lang).text # Translate the clean text
                    
                    translated_data.append({
                        'question': translated_question,
                        # Note: The translated answer will no longer have <p> tags
                        'answer': translated_answer
                    })
                except Exception as e:
                    print(f"Translation Error: {e}")
                    translated_data.append(item)
            data = translated_data

        cache.set(cache_key, data, 60 * 15)
        return Response(data)