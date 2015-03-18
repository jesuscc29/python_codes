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

// Javascript to enable link to tab
var url = document.location.toString();
if (url.match('#')) {
    $('.nav-tabs a[href=#' + url.split('#')[1] + ']').tab('show');
}
// Change hash for page-reload
           $('.nav-tabs a').on('click', function (e) {
               window.location.hash = e.target.hash;
           });
           
/* Function to autocomplete on input field based on a query
* This example is based on Django.
* See __init__.py to see the Django/Python code
*/

$(function () {
            $("#id_service").autocomplete({
                minLength: 3,
                source: function (req, add) {
                    $.ajax({
                        url: '{% url "autocomplete_services" %}',
                        async: false,
                        dataType: 'json',
                        type: 'POST',
                        data: {
                            service: function () {
                                return $("#id_service").val();
                            },
                            'csrfmiddlewaretoken': '{{ csrf_token }}'
                        },
                        success: function (data) {

                            //create array for response objects
                            var suggestions = [];

                            data.forEach(function(item) {
                                //console.log(item['service']);
                                suggestions.push(item['service']);
                            });

                            console.log(suggestions);
                            //pass array to callback
                            add(suggestions);
                        }
                    });
                }
            });
        });
