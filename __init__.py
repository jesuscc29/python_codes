import time
import datetime


def date_time_functions():
  """
  Usage of datetime functions
  """
  print "Time in seconds since the epoch: %s" %time.time()
  print "Current date and time: " , datetime.datetime.now()
  print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
  
  print "Current year: ", datetime.date.today().strftime("%Y")
  print "Month of year: ", datetime.date.today().strftime("%B")
  print "Week number of the year: ", datetime.date.today().strftime("%W")
  print "Weekday of the week: ", datetime.date.today().strftime("%w")
  print "Day of year: ", datetime.date.today().strftime("%j")
  print "Day of the month : ", datetime.date.today().strftime("%d")
  print "Day of week: ", datetime.date.today().strftime("%A")
  
  
  def edit_deal(request, deal_slug):
    """ This method is an example of how to save a file with ajax.
    ajax code:
    function upload(event) {
      event.preventDefault();
      var data = new FormData($('#editDealForm').get(0));

        $.ajax({
          url: "{% url "edit_deal" deal_slug=deal_info.deal_slug %}",
          type: "post",
          data: data,
          cache: false,
          processData: false,
          contentType: false,
          success: function (data) {
            alert("Deal editado corretamente");
            $("#editDealForm").trigger("reset");
            document.location.reload();
          }
        });
      return false;
    }

    $(function () {
      $('#editDealForm').submit(upload);
    });
    """
    deal = Deal.objects.get(slug=deal_slug)
    form = DealForm(data=request.POST or None, files=request.FILES or None,
                    instance=deal)
    if form.is_valid():
        form.save()
        add_auto_activity(deal_slug, 'Modificación', deal.manager)
        return HttpResponseRedirect(reverse('deal_detail',
                                            kwargs={'deal_slug': deal_slug}))
    else:
        print form.errors
        
def user_login(request):
    error = ''
    if request.user.is_authenticated():
        return HttpResponseRedirect("/main/")
    if request.method == "POST":
        if 'email' in request.POST and request.POST['email']:
            if is_valid_email(request.POST['email']):
                #reset password
                reset_pass(request.POST['email'])
                error = "En breve recibirá un correo con su nueva contraseña."
            else:
                error = 'El correo proporcionado no es v&aacute;lido'
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if 'rememberme' not in request.POST:
                        request.session.set_expiry(300)
 
                    login(request, user)
                    url = "/main/"
                    try:
                        ur_get = request.META['HTTP_REFERER']
                    except KeyError:
                        pass
                    else:
                        ur_get = ur_get.split("next=")
                        if len(ur_get) > 1:
                            url = ur_get[1]
                    return HttpResponseRedirect(url)
                else:
                    error = "Tu cuenta ha sido desactivada, por favor " \
                            "ponte en contacto con tu administrador"
            else:
                error = "Tu nombre de usuario o contrase&ntilde;a son " \
                        "incorrectos."
    institution = settings.PROJECT_NAME
    variables = dict(error=error,
                     institution=institution)
    variables_template = RequestContext(request, variables)
    return render_to_response("login.html", variables_template)
 
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/main/')
 
 
def reset_pass(email):
    new_pass = random_string_generator()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        pass
    else:
        user.set_password(new_pass)
        domain = settings.DOMAIN
        url_sys = 'http://'+domain
        subject, from_email, to = 'Reseteo de contraseña', \
                                  'noresponse@{0}'.format(domain), email
        text_content = 'Su contraseña ha sido restablecida, puede ingresar ' \
                       'al sistema ({0}) con su nombre de usuario y ' \
                       'la contraseña: {1} \n Una vez dentro del sistema, ' \
                       'podrá cambiar su contraseña por la que usted desee'\
            .format(url_sys, new_pass)
        html_content = '<h1>Su contraseña ha sido restablecida</h1>' \
                       '<p>Puede ingresar al <a href="{0}">sistema escolar ' \
                       'con su nombre de usuario y contraseña:</p>' \
                       '<p style="text-align:center;">{1}</p>' \
                       '<p>Una vez dentro del sistema, podrá cambiar su ' \
                       'contraseña por la que usted desee</p>'\
            .format(url_sys, new_pass)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        try:
            msg.send()
        except error:
            print "Is the email server online?"
 
    return
# @cache_page(None)  # won't expire, ever
def dyn_css(request):
    css_theme = SystemSettings.objects.get(pk=1)
    return render_to_response('static/theme/css/style.css', {'theme': css_theme},
                              content_type="text/css")
                              
def reset_cache(request, view='dyn_css', args=None):
    from django.core.cache import cache
    from django.utils.cache import get_cache_key

    if args is None:
        path = reverse(view)
    else:
        path = reverse(view, args=args)

    request.path = path
    key = get_cache_key(request)
    if key in cache:
        cache.delete(key)
        
  # ++==================================================================++
def get_initial(self):
    """
    This function can be inside of a  Class Based View to access the request
    variable
    """
    user = self.request.user
    permission = False
    if has_permissions(user, 'Proyectos', 'Consulta'):
        permission = True
    return permission
    
    
from datetime import datetime, timedelta

    def week_of_month(date):
      """ gets the number of week of a current date
      """
        month = date.month
        week = 0
        while date.month == month:
            week += 1
            date -= timedelta(days=7)

        return week
