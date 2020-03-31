$(document).on('submit', '#ajouter_consultant',function(e)
{
    e.preventDefault();
    $.ajax(
    {
        type:'POST',
        url:'administrateur/consultant',    
        data:
        {
            nom_consultant:$('#nom_consultant').val(),
            prenom_consultant:$('#prenom_consultant').val(),
            email_consultant:$('#email_consultant').val(),
            telephone_consultant:$('#telephone_consultant').val(),
            diminutif_consultant:$('#diminutif_consultant').val(),
            adresse_consultant:$('#adresse_consultant').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'ajouter_consultant'
        },
        success:function(json)
        {
            document.getElementById("close_modal").click();
            var date_joined = json.date_joined_consultant;
            var last_login = json.last_login_consultant;
            var options = {year: 'numeric', month: 'long', day: 'numeric',hour: 'numeric', minute:'numeric'};
            if (date_joined != "None")
            {
                date_joined = new Date(date_joined)
                date_joined = date_joined.toLocaleDateString('fr-FR',options);
            }
            if (last_login != "None")
            {
                last_login = new Date(last_login)
                last_login = last_login.toLocaleDateString('fr-FR',options);
            }
            var badge_actif = "";
            if (json.is_active==true)
            {
                badge_actif = `<span class="kt-badge kt-badge--info kt-badge--inline">Actif</span>`;
            }
            else
            {
                badge_actif = `<span class="badge badge-secondary">Inactif</span>`;
            }
            var badge_online = "";
            if (json.is_online==true)
            {
                badge_online = `<span class="kt-badge kt-badge--success kt-badge--dot"></span>
                                <span class="kt-font-bold kt-font-success"> En ligne</span>`;
            }
            else
            {
                badge_online = `<span class="kt-badge kt-badge--danger kt-badge--dot"></span>
                                <span class="kt-font-bold kt-font-danger"> Hors ligne</span>`;
            }
            var csrf = "{% csrf_token %}"
            document.getElementById("ajouter_consultant").reset();
            $("tbody").prepend(`
                <tr role="row" class="odd">
                    <td>
                        <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid" for="` + json.id_consultant + `">
                            <input type="checkbox" value="` + json.id_consultant + `" id="` + json.id_consultant + `" name="consultant_selectionne" class="kt-checkable">
                            <span></span>
                        </label>
                    </td>
                    <td>
                        <span>
                            <div class="kt-user-card-v2">
                                <div class="kt-user-card-v2__pic">
                                    <img src="` + json.avatar_consultant + `" alt="photo">
                                </div>
                                <div class="kt-user-card-v2__details">
                                    <a href="#" class="kt-user-card-v2__name">` + json.prenom_consultant + ` ` + json.nom_consultant + `</a>
                                    <span class="kt-user-card-v2__desc">` + json.group_consultant + `</span>
                                </div>
                            </div>
                        </span>
                    </td>
                    <td>
                        <a class="kt-link" href="mailto:` + json.email_consultant + `">` + json.email_consultant + `</a>
                        <br>
                        <a class="kt-link" href="tel:`+ json.telephone_consultant +`">` + json.telephone_consultant + `</a>
                    </td>
                    <td>` + date_joined + `</td>
                    <td>` + last_login + `</td>
                    <td>` + badge_actif + `</td>
                    <td>` + badge_online + `</td>
                    <td>
                        <a id="button" href="/administrateur/profil_consultant/` + json.id_consultant + `" class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" title="Profil du consultant">
                            <i class="icon-eye"></i>
                        </a>
                        <a class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" alt="Supprimer" title="Supprimer le consultant" data-id=` + json.id_consultant + `>
                            <i class="icon-trash"></i>
                        </a>
                    </td>
                </tr>`
            )
            $("#kt_wrapper").prepend(`
                <ul class="messagelist">
                    <div class="alert alert-success alert-dismissible" role="alert">
                        <button type="button" class="close pclose-btn-alert" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    Le consultant a bien été créé.
                    </div>
                </ul>`
            )
        },
        error : function(xhr,errmsg,err)
        {
            $('#results').html(`
                <div class='alert-box alert radius' data-alert>
                    Oops! We have encountered an error: ` + errmsg + `
                    <a href='#' class='close'>&times;</a>
                </div>`); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});
$(document).on('submit', '#form_taleau_consultant',function(e)
{
    var buttonpressed = this;
    var buttonpressed_name = this.name;
    var buttonpressed_id = this.getAttribute('data-id');
    e.preventDefault();
    $.ajax(
    {
        type:'POST',
        url:'{% url "consultant" %}',
        data:
        {
            id:buttonpressed_id,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: buttonpressed_name
        },
        success:function(json)
        {
            document.getElementById("form_taleau_consultant").reset();
            $("#supprimer_consultant_"+json.id_consultant).parent().parent().remove();
        },
        error : function(xhr,errmsg,err)
        {
            $('#results').html(`
                <div class='alert-box alert radius' data-alert>
                    Oops! We have encountered an error: ` + errmsg + `
                    <a href='#' class='close'>&times;</a>
                </div>`); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});