"use strict";
var KTAppChat = function() {
    var t;
    return {
        init: function() {
            t = KTUtil.getByID("kt_chat_aside"),
                function() {
                    new KTOffcanvas(t, {
                        overlay: !0,
                        baseClass: "kt-app__aside",
                        closeBy: "kt_chat_aside_close",
                        toggleBy: "kt_chat_aside_mobile_toggle"
                    });
                    var i = KTUtil.find(t, ".kt-scroll");
                    i && KTUtil.scrollInit(i, {
                        mobileNativeScroll: !0,
                        desktopNativeScroll: !1,
                        resetHeightOnDestroy: !0,
                        handleWindowResize: !0,
                        rememberPosition: !0,
                        height: function() {
                            var i, s = KTUtil.find(t, ".kt-portlet > .kt-portlet__body"),
                                e = KTUtil.find(t, ".kt-widget.kt-widget--users"),
                                n = KTUtil.find(t, ".kt-searchbar");
                            return i = KTUtil.isInResponsiveRange("desktop") ? KTLayout.getContentHeight() : KTUtil.getViewPort().height, t && (i = (i = i - parseInt(KTUtil.css(t, "margin-top")) - parseInt(KTUtil.css(t, "margin-bottom"))) - parseInt(KTUtil.css(t, "padding-top")) - parseInt(KTUtil.css(t, "padding-bottom"))), e && (i = (i = i - parseInt(KTUtil.css(e, "margin-top")) - parseInt(KTUtil.css(e, "margin-bottom"))) - parseInt(KTUtil.css(e, "padding-top")) - parseInt(KTUtil.css(e, "padding-bottom"))), s && (i = (i = i - parseInt(KTUtil.css(s, "margin-top")) - parseInt(KTUtil.css(s, "margin-bottom"))) - parseInt(KTUtil.css(s, "padding-top")) - parseInt(KTUtil.css(s, "padding-bottom"))), n && (i = (i -= parseInt(KTUtil.css(n, "height"))) - parseInt(KTUtil.css(n, "margin-top")) - parseInt(KTUtil.css(n, "margin-bottom"))), i -= 5
                        }
                    })
                }(), KTChat.setup(KTUtil.getByID("kt_chat_content")), KTUtil.getByID("kt_app_chat_launch_btn") && setTimeout(function() {
                    KTUtil.getByID("kt_app_chat_launch_btn").click()
                }, 1e3)
        }
    }
}();
KTUtil.ready(function() {
    KTAppChat.init()
});