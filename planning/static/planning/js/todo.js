"use strict";
var KTAppTodo = function() {
    var t, e, o;
    return {
        init: function() {
            t = KTUtil.getByID("kt_todo_aside"), e = KTUtil.getByID("kt_todo_list"), o = KTUtil.getByID("kt_todo_view"), KTAppTodo.initAside(), KTAppTodo.initList(), KTAppTodo.initCommentForm(), KTAppTodo.initView()
        },
        initAside: function() {
            new KTOffcanvas(t, {
                overlay: !0,
                baseClass: "kt-todo__aside",
                closeBy: "kt_todo_aside_close",
                toggleBy: "kt_subheader_mobile_toggle"
            })
        },
        initList: function() {
            KTUtil.on(e, ".kt-todo__item", "click", function(t) {
                var i = KTUtil.find(this, ".kt-todo__actions");
                if (t.target === i || i && !0 === i.contains(t.target)) return !1;
                if (!1 !== KTUtil.isInResponsiveRange("tablet-and-mobile")) {
                    var n = new KTDialog({
                        type: "loader",
                        placement: "top center",
                        message: "Loading ..."
                    });
                    n.show(), setTimeout(function() {
                        n.hide(), KTUtil.css(e, "display", "none"), KTUtil.css(o, "display", "flex")
                    }, 700)
                }
            }), KTUtil.on(e, ".kt-todo__toolbar .kt-todo__check .kt-checkbox input", "click", function() {
                for (var t = KTUtil.findAll(e, ".kt-todo__items .kt-todo__item"), o = 0, i = t.length; o < i; o++) {
                    var n = t[o];
                    KTUtil.find(n, ".kt-todo__actions .kt-checkbox input").checked = this.checked, this.checked ? KTUtil.addClass(n, "kt-todo__item--selected") : KTUtil.removeClass(n, "kt-todo__item--selected")
                }
            }), KTUtil.on(e, ".kt-todo__item .kt-checkbox input", "click", function() {
                var t = this.closest(".kt-todo__item");
                t && this.checked ? KTUtil.addClass(t, "kt-todo__item--selected") : KTUtil.removeClass(t, "kt-todo__item--selected")
            })
        },
        initView: function() {
            KTUtil.on(o, ".kt-todo__toolbar .kt-todo__icon.kt-todo__icon--back", "click", function() {
                var t = new KTDialog({
                    type: "loader",
                    placement: "top center",
                    message: "Loading ..."
                });
                t.show(), setTimeout(function() {
                    t.hide(), KTUtil.css(e, "display", "flex"), KTUtil.css(o, "display", "none")
                }, 700)
            })
        },
        initCommentForm: function() {
            var t;
            t = "kt_todo_post_editor", t = new Quill("#" + t, {
                    modules: {
                        toolbar: {}
                    },
                    placeholder: "Type message...",
                    theme: "snow"
                }),
                function(t) {
                    var e = "#" + t,
                        o = $(e + " .dropzone-item");
                    o.id = "";
                    var i = o.parent(".dropzone-items").html();
                    o.remove();
                    var n = new Dropzone(e, {
                        url: "",
                        parallelUploads: 20,
                        maxFilesize: 1,
                        previewTemplate: i,
                        previewsContainer: e + " .dropzone-items",
                        clickable: e + "_select"
                    });
                    n.on("addedfile", function(t) {
                        $(document).find(e + " .dropzone-item").css("display", "")
                    }), n.on("totaluploadprogress", function(t) {
                        document.querySelector(e + " .progress-bar").style.width = t + "%"
                    }), n.on("sending", function(t) {
                        document.querySelector(e + " .progress-bar").style.opacity = "1"
                    }), n.on("complete", function(t) {
                        var o = e + " .dz-complete";
                        setTimeout(function() {
                            $(o + " .progress-bar, " + o + " .progress").css("opacity", "0")
                        }, 300)
                    })
                }("kt_todo_post_attachments")
        }
    }
}();
KTUtil.ready(function() {
    KTAppTodo.init()
});