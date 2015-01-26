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
