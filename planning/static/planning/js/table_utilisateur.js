$(document).ready(function() 
{
    //Create the table
    var table = $('#kt_table').DataTable
    ( 
        {
            "ajax": 
            {
                "url": "/ajax_utilisateurs",
                "type": "GET",
                "dataType": "json",
                "async": true,
                "dataSrc": ""
            },
            "order": [[ 1, "asc" ]],
            "language": 
            {
                "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/French.json"
            },
            "columns": 
            [
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        return (`
                            <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid" for="` + id + `">
                                <input type="checkbox" value="` + id + `" id="` + id + `" name="utilisateur_selectionne" class="kt-checkable">
                                <span></span>
                            </label>`);
                    },
                    "orderable": false,
                    "width": "1%",
                },
                {
                    "render": function ( data, type, row )
                    {
                        var nom = row.fields.last_name;
                        var prenom = row.fields.first_name;
                        var group = row.fields.groups;
                        var url_profil = "/profil_utilisateur/" + row.pk;
                        if ( row.fields.avatar != null)
                        {
                            var avatar = row.fields.avatar;
                            return (`
                                <span>
                                    <div class="kt-user-card-v2">
                                        <div class="kt-user-card-v2__pic">
                                            <img src="` + avatar + `" alt="photo">
                                        </div>
                                        <div class="kt-user-card-v2__details">
                                            <a href="` + url_profil + `" class="kt-user-card-v2__name">` + prenom + ` ` + nom + `</a>
                                            <span class="kt-user-card-v2__desc">` + group + `</span>
                                        </div>
                                    </div>
                                </span>`);
                        }
                        else
                        {
                            var diminutif = row.fields.diminutif;
                            var color_rdm = row.fields.couleur_rdm;
                            return (`
                                <span>
                                    <div class="kt-user-card-v2">
                                        <div class="kt-user-card-v2__pic" style="background-color:`+color_rdm+`30;">
                                            <span style="color:`+color_rdm+`;font-weight:bold;">` + diminutif + `</span>
                                        </div>
                                        <div class="kt-user-card-v2__details">
                                            <a href="` + url_profil + `" class="kt-user-card-v2__name">` + prenom + ` ` + nom + `</a>
                                            <span class="kt-user-card-v2__desc">` + group + `</span>
                                        </div>
                                    </div>
                                </span>`);
                        }
                        
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var email = row.fields.email;
                        var telephone = row.fields.telephone;
                        return (`
                            <a class="kt-link" href="mailto:` + email + `">` + email + `</a>
                            <br>
                            <a class="kt-link" href="tel:`+ telephone +`">` + telephone + `</a>`);
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var date_joined = row.fields.date_joined;
                        var res = '';
                        if (date_joined != "None")
                        {
                            var options = {year: 'numeric', month: 'long', day: 'numeric',hour: 'numeric', minute:'numeric'};
                            var date_joined = new Date(date_joined)
                            res += date_joined.toLocaleDateString('fr-FR',options);
                        }
                        return res; 
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var last_login = row.fields.last_login;
                        var res = '';
                        if (last_login != "None")
                        {
                            var options = {year: 'numeric', month: 'numeric', day: 'numeric'};
                            var last_login = new Date(last_login)
                            res += last_login.toLocaleDateString('fr-FR',options);
                        }
                        return res;
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        var is_active = row.fields.is_active;
                        var res = '';
                        if (is_active == true)
                        {
                            return (`<span class="kt-badge kt-badge--info kt-badge--inline" id="active_`+id+`">Actif</span>`);
                        }
                        else
                        {
                            return (`<span class="badge badge-secondary" id="active_`+id+`">Inactif</span>`);
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var csrf = "{% csrf_token %}"
                        var id = row.pk;
                        var nom = row.fields.last_name;
                        var prenom = row.fields.first_name;
                        var url_profil = "/profil_utilisateur/" + id;
                        var is_active = row.fields.is_active;
                        return (`
                            <a id="button" href="` + url_profil + `" class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" title="Profil de l'utilisateur">
                                <i class="icon-eye"></i>
                            </a>
                            <a class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" onclick="openModalDelete('` + nom + ` ` + prenom +`',` + id + `)" id="supprimer_utilisateur_` + id + `" alt="Supprimer" title="Supprimer l'utilisateur" data-id=` + id + `>
                                <i class="icon-trash"></i>
                            </a>`);
                    }

                }
            ]
        }
    );

    // Check/uncheck all checkboxes in the table
    $('#select_all1').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all2').checked == true)
        {
            document.getElementById('select_all2').checked = false;
        }
        else
        {
            document.getElementById('select_all2').checked = true;
        }
    });

    // Check/uncheck all checkboxes in the table
    $('#select_all2').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all1').checked == true)
        {
            document.getElementById('select_all1').checked = false;
        }
        else
        {
            document.getElementById('select_all1').checked = true;
        }
    });

    // When a checkboxe is cheked display menu
    $('#kt_table').on('click',"input[type='checkbox']", function()
    {
        var nombre_row_checked = $('input[name="utilisateur_selectionne"]:checked').length;
        var total_rows = table.rows().count()
        if (nombre_row_checked > 0)
        {
            document.getElementById("nombre_de_utilisateur").innerHTML = nombre_row_checked + " sélectionnées";
            document.getElementById('menu_to_display').style.display = 'flex';
        }
        else
        {
            document.getElementById("nombre_de_utilisateur").innerHTML = total_rows + " total";
            document.getElementById('menu_to_display').style.display = 'none';
        }
        var row = $(this).closest('tr');
        if(this.checked)
        {
            row.addClass('selected');
        } 
        else 
        {
            row.removeClass('selected');
        }     
    });
});