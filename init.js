function validateRequiredFields(form) {
  var is_valid = false;
  form.find("input.required, select.required").each(
    function (index) {
      var $this = $(this);
      var parent = $this.parent();
      if ($this.val() == '' || $this.val() == 0) {
        parent.removeClass('has-success');
        parent.addClass('has-error');
        is_valid = false;
      } else {
        parent.removeClass('has-error');
        parent.addClass('has-success');
        is_valid = true;
      }
    });
    return is_valid;
  }
  
/* Do Ajax While Typing */  
delay(function () {
        var text = $("#searchClient").val();
        if (text != '') {
                e.preventDefault();
                $.ajax({
                        type: "post",
                        url: "{% url "search_client" %}",
                        data: {
                                'text': text,
                                'csrfmiddlewaretoken': '{{ csrf_token }}'
                        },
                        success: function (data) {
                                console.log(data);
                        },
                        error: function (data) {
                                console.log(data);
                        }
                });
        } else {
                //$("#table-data").hide();
        }
}, 900);
