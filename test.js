window = global;
document = {
    location: {
        origin: "https://arcteryx.com Permitted src= https://checkoutshopper-live.adyen.com/checkoutshopper/securedfields/live_36ZB7DYZZJBQVI4577ERRX4C3AFQPTSV/4.9.0/securedFields.html"
    }
}
!(function() {
    var origin = "https://arcteryx.com";
    var originKey = "live_36ZB7DYZZJBQVI4577ERRX4C3AFQPTSV";
    var genTime = "2025-06-29T12:27:40Z";
    var checkoutShopperUrl = "https://checkoutshopper-live.adyen.com/checkoutshopper/";

    var adyen = window.adyen = window.adyen || {};
    adyen.key = "10001|C182E36FF4C509A1624CFFEE711F4C2189F07D22245AB41B23E499C46EAD5F2172BDA021F65E147EB83EA5CC5F11D192286757E5C513120D34F15607F368DC17678F027EE44B0DE6FC173C8AF4472D478507E2C0F88D1A9E0E9B379F48070D154459CA672F17269F1DED3C29DFA439F14FB245C33FCFBE4D5A0FE4E18F95BE7D1A07E4906679517756F815BF71C8746C21BAC98A687805B4095E1945EADA5BC46D2AC1691CCCBCCFCB5F4B4AE443E7F6D0F74491CDB433E7205D37D75E77EF38AEE2C09CAF7CCAA81D6FD6BD1896DC7D47E345F8FD8510F9C15BB78CAEBA5944C0D01CABF7A0E58AD8E7D94EBA4775B5202A36111B5441E46845B83F2E501A89";

    /*!
* 
*             ***********
*             securedFields-giftcard version: 4.9.0
*             ***********
*
*/
    ( () => {
        var e = {
            666: e => {
                var t = function(e) {
                    "use strict";
                    var t, r = Object.prototype, n = r.hasOwnProperty, o = Object.defineProperty || function(e, t, r) {
                        e[t] = r.value
                    }
                    , i = "function" == typeof Symbol ? Symbol : {}, a = i.iterator || "@@iterator", c = i.asyncIterator || "@@asyncIterator", s = i.toStringTag || "@@toStringTag";
                    function u(e, t, r) {
                        return Object.defineProperty(e, t, {
                            value: r,
                            enumerable: !0,
                            configurable: !0,
                            writable: !0
                        }),
                        e[t]
                    }
                    try {
                        u({}, "")
                    } catch (e) {
                        u = function(e, t, r) {
                            return e[t] = r
                        }
                    }
                    function l(e, t, r, n) {
                        var i = t && t.prototype instanceof b ? t : b
                          , a = Object.create(i.prototype)
                          , c = new C(n || []);
                        return o(a, "_invoke", {
                            value: k(e, r, c)
                        }),
                        a
                    }
                    function f(e, t, r) {
                        try {
                            return {
                                type: "normal",
                                arg: e.call(t, r)
                            }
                        } catch (e) {
                            return {
                                type: "throw",
                                arg: e
                            }
                        }
                    }
                    e.wrap = l;
                    var p = "suspendedStart"
                      , d = "suspendedYield"
                      , h = "executing"
                      , y = "completed"
                      , v = {};
                    function b() {}
                    function g() {}
                    function m() {}
                    var w = {};
                    u(w, a, (function() {
                        return this
                    }
                    ));
                    var _ = Object.getPrototypeOf
                      , O = _ && _(_(R([])));
                    O && O !== r && n.call(O, a) && (w = O);
                    var S = m.prototype = b.prototype = Object.create(w);
                    function P(e) {
                        ["next", "throw", "return"].forEach((function(t) {
                            u(e, t, (function(e) {
                                return this._invoke(t, e)
                            }
                            ))
                        }
                        ))
                    }
                    function E(e, t) {
                        function r(o, i, a, c) {
                            var s = f(e[o], e, i);
                            if ("throw" !== s.type) {
                                var u = s.arg
                                  , l = u.value;
                                return l && "object" == typeof l && n.call(l, "__await") ? t.resolve(l.__await).then((function(e) {
                                    r("next", e, a, c)
                                }
                                ), (function(e) {
                                    r("throw", e, a, c)
                                }
                                )) : t.resolve(l).then((function(e) {
                                    u.value = e,
                                    a(u)
                                }
                                ), (function(e) {
                                    return r("throw", e, a, c)
                                }
                                ))
                            }
                            c(s.arg)
                        }
                        var i;
                        o(this, "_invoke", {
                            value: function(e, n) {
                                function o() {
                                    return new t((function(t, o) {
                                        r(e, n, t, o)
                                    }
                                    ))
                                }
                                return i = i ? i.then(o, o) : o()
                            }
                        })
                    }
                    function k(e, t, r) {
                        var n = p;
                        return function(o, i) {
                            if (n === h)
                                throw new Error("Generator is already running");
                            if (n === y) {
                                if ("throw" === o)
                                    throw i;
                                return I()
                            }
                            for (r.method = o,
                            r.arg = i; ; ) {
                                var a = r.delegate;
                                if (a) {
                                    var c = A(a, r);
                                    if (c) {
                                        if (c === v)
                                            continue;
                                        return c
                                    }
                                }
                                if ("next" === r.method)
                                    r.sent = r._sent = r.arg;
                                else if ("throw" === r.method) {
                                    if (n === p)
                                        throw n = y,
                                        r.arg;
                                    r.dispatchException(r.arg)
                                } else
                                    "return" === r.method && r.abrupt("return", r.arg);
                                n = h;
                                var s = f(e, t, r);
                                if ("normal" === s.type) {
                                    if (n = r.done ? y : d,
                                    s.arg === v)
                                        continue;
                                    return {
                                        value: s.arg,
                                        done: r.done
                                    }
                                }
                                "throw" === s.type && (n = y,
                                r.method = "throw",
                                r.arg = s.arg)
                            }
                        }
                    }
                    function A(e, r) {
                        var n = e.iterator[r.method];
                        if (n === t) {
                            if (r.delegate = null,
                            "throw" === r.method) {
                                if (e.iterator.return && (r.method = "return",
                                r.arg = t,
                                A(e, r),
                                "throw" === r.method))
                                    return v;
                                r.method = "throw",
                                r.arg = new TypeError("The iterator does not provide a 'throw' method")
                            }
                            return v
                        }
                        var o = f(n, e.iterator, r.arg);
                        if ("throw" === o.type)
                            return r.method = "throw",
                            r.arg = o.arg,
                            r.delegate = null,
                            v;
                        var i = o.arg;
                        return i ? i.done ? (r[e.resultName] = i.value,
                        r.next = e.nextLoc,
                        "return" !== r.method && (r.method = "next",
                        r.arg = t),
                        r.delegate = null,
                        v) : i : (r.method = "throw",
                        r.arg = new TypeError("iterator result is not an object"),
                        r.delegate = null,
                        v)
                    }
                    function x(e) {
                        var t = {
                            tryLoc: e[0]
                        };
                        1 in e && (t.catchLoc = e[1]),
                        2 in e && (t.finallyLoc = e[2],
                        t.afterLoc = e[3]),
                        this.tryEntries.push(t)
                    }
                    function j(e) {
                        var t = e.completion || {};
                        t.type = "normal",
                        delete t.arg,
                        e.completion = t
                    }
                    function C(e) {
                        this.tryEntries = [{
                            tryLoc: "root"
                        }],
                        e.forEach(x, this),
                        this.reset(!0)
                    }
                    function R(e) {
                        if (e) {
                            var r = e[a];
                            if (r)
                                return r.call(e);
                            if ("function" == typeof e.next)
                                return e;
                            if (!isNaN(e.length)) {
                                var o = -1
                                  , i = function r() {
                                    for (; ++o < e.length; )
                                        if (n.call(e, o))
                                            return r.value = e[o],
                                            r.done = !1,
                                            r;
                                    return r.value = t,
                                    r.done = !0,
                                    r
                                };
                                return i.next = i
                            }
                        }
                        return {
                            next: I
                        }
                    }
                    function I() {
                        return {
                            value: t,
                            done: !0
                        }
                    }
                    return g.prototype = m,
                    o(S, "constructor", {
                        value: m,
                        configurable: !0
                    }),
                    o(m, "constructor", {
                        value: g,
                        configurable: !0
                    }),
                    g.displayName = u(m, s, "GeneratorFunction"),
                    e.isGeneratorFunction = function(e) {
                        var t = "function" == typeof e && e.constructor;
                        return !!t && (t === g || "GeneratorFunction" === (t.displayName || t.name))
                    }
                    ,
                    e.mark = function(e) {
                        return Object.setPrototypeOf ? Object.setPrototypeOf(e, m) : (e.__proto__ = m,
                        u(e, s, "GeneratorFunction")),
                        e.prototype = Object.create(S),
                        e
                    }
                    ,
                    e.awrap = function(e) {
                        return {
                            __await: e
                        }
                    }
                    ,
                    P(E.prototype),
                    u(E.prototype, c, (function() {
                        return this
                    }
                    )),
                    e.AsyncIterator = E,
                    e.async = function(t, r, n, o, i) {
                        void 0 === i && (i = Promise);
                        var a = new E(l(t, r, n, o),i);
                        return e.isGeneratorFunction(r) ? a : a.next().then((function(e) {
                            return e.done ? e.value : a.next()
                        }
                        ))
                    }
                    ,
                    P(S),
                    u(S, s, "Generator"),
                    u(S, a, (function() {
                        return this
                    }
                    )),
                    u(S, "toString", (function() {
                        return "[object Generator]"
                    }
                    )),
                    e.keys = function(e) {
                        var t = Object(e)
                          , r = [];
                        for (var n in t)
                            r.push(n);
                        return r.reverse(),
                        function e() {
                            for (; r.length; ) {
                                var n = r.pop();
                                if (n in t)
                                    return e.value = n,
                                    e.done = !1,
                                    e
                            }
                            return e.done = !0,
                            e
                        }
                    }
                    ,
                    e.values = R,
                    C.prototype = {
                        constructor: C,
                        reset: function(e) {
                            if (this.prev = 0,
                            this.next = 0,
                            this.sent = this._sent = t,
                            this.done = !1,
                            this.delegate = null,
                            this.method = "next",
                            this.arg = t,
                            this.tryEntries.forEach(j),
                            !e)
                                for (var r in this)
                                    "t" === r.charAt(0) && n.call(this, r) && !isNaN(+r.slice(1)) && (this[r] = t)
                        },
                        stop: function() {
                            this.done = !0;
                            var e = this.tryEntries[0].completion;
                            if ("throw" === e.type)
                                throw e.arg;
                            return this.rval
                        },
                        dispatchException: function(e) {
                            if (this.done)
                                throw e;
                            var r = this;
                            function o(n, o) {
                                return c.type = "throw",
                                c.arg = e,
                                r.next = n,
                                o && (r.method = "next",
                                r.arg = t),
                                !!o
                            }
                            for (var i = this.tryEntries.length - 1; i >= 0; --i) {
                                var a = this.tryEntries[i]
                                  , c = a.completion;
                                if ("root" === a.tryLoc)
                                    return o("end");
                                if (a.tryLoc <= this.prev) {
                                    var s = n.call(a, "catchLoc")
                                      , u = n.call(a, "finallyLoc");
                                    if (s && u) {
                                        if (this.prev < a.catchLoc)
                                            return o(a.catchLoc, !0);
                                        if (this.prev < a.finallyLoc)
                                            return o(a.finallyLoc)
                                    } else if (s) {
                                        if (this.prev < a.catchLoc)
                                            return o(a.catchLoc, !0)
                                    } else {
                                        if (!u)
                                            throw new Error("try statement without catch or finally");
                                        if (this.prev < a.finallyLoc)
                                            return o(a.finallyLoc)
                                    }
                                }
                            }
                        },
                        abrupt: function(e, t) {
                            for (var r = this.tryEntries.length - 1; r >= 0; --r) {
                                var o = this.tryEntries[r];
                                if (o.tryLoc <= this.prev && n.call(o, "finallyLoc") && this.prev < o.finallyLoc) {
                                    var i = o;
                                    break
                                }
                            }
                            i && ("break" === e || "continue" === e) && i.tryLoc <= t && t <= i.finallyLoc && (i = null);
                            var a = i ? i.completion : {};
                            return a.type = e,
                            a.arg = t,
                            i ? (this.method = "next",
                            this.next = i.finallyLoc,
                            v) : this.complete(a)
                        },
                        complete: function(e, t) {
                            if ("throw" === e.type)
                                throw e.arg;
                            return "break" === e.type || "continue" === e.type ? this.next = e.arg : "return" === e.type ? (this.rval = this.arg = e.arg,
                            this.method = "return",
                            this.next = "end") : "normal" === e.type && t && (this.next = t),
                            v
                        },
                        finish: function(e) {
                            for (var t = this.tryEntries.length - 1; t >= 0; --t) {
                                var r = this.tryEntries[t];
                                if (r.finallyLoc === e)
                                    return this.complete(r.completion, r.afterLoc),
                                    j(r),
                                    v
                            }
                        },
                        catch: function(e) {
                            for (var t = this.tryEntries.length - 1; t >= 0; --t) {
                                var r = this.tryEntries[t];
                                if (r.tryLoc === e) {
                                    var n = r.completion;
                                    if ("throw" === n.type) {
                                        var o = n.arg;
                                        j(r)
                                    }
                                    return o
                                }
                            }
                            throw new Error("illegal catch attempt")
                        },
                        delegateYield: function(e, r, n) {
                            return this.delegate = {
                                iterator: R(e),
                                resultName: r,
                                nextLoc: n
                            },
                            "next" === this.method && (this.arg = t),
                            v
                        }
                    },
                    e
                }(e.exports);
                try {
                    regeneratorRuntime = t
                } catch (e) {
                    "object" == typeof globalThis ? globalThis.regeneratorRuntime = t : Function("r", "regeneratorRuntime = r")(t)
                }
            }
        }
          , t = {};
        function r(n) {
            var o = t[n];
            if (void 0 !== o)
                return o.exports;
            var i = t[n] = {
                exports: {}
            };
            console.log(n)
            return e[n](i, i.exports, r),
            i.exports
        }
        ( () => {
            "use strict";
            r(666);
            var e, t, n, o, i, a, c, s = {}, u = [], l = /acit|ex(?:s|g|n|p|$)|rph|grid|ows|mnc|ntw|ine[ch]|zoo|^ord|itera/i;
            function f(e, t) {
                for (var r in t)
                    e[r] = t[r];
                return e
            }
            function p(e) {
                var t = e.parentNode;
                t && t.removeChild(e)
            }
            function d(t, r, n) {
                var o, i, a, c = {};
                for (a in r)
                    "key" == a ? o = r[a] : "ref" == a ? i = r[a] : c[a] = r[a];
                if (arguments.length > 2 && (c.children = arguments.length > 3 ? e.call(arguments, 2) : n),
                "function" == typeof t && null != t.defaultProps)
                    for (a in t.defaultProps)
                        void 0 === c[a] && (c[a] = t.defaultProps[a]);
                return h(t, c, o, i, null)
            }
            function h(e, r, o, i, a) {
                var c = {
                    type: e,
                    props: r,
                    key: o,
                    ref: i,
                    __k: null,
                    __: null,
                    __b: 0,
                    __e: null,
                    __d: void 0,
                    __c: null,
                    __h: null,
                    constructor: void 0,
                    __v: null == a ? ++n : a
                };
                return null == a && null != t.vnode && t.vnode(c),
                c
            }
            function y(e) {
                return e.children
            }
            function v(e, t) {
                this.props = e,
                this.context = t
            }
            function b(e, t) {
                if (null == t)
                    return e.__ ? b(e.__, e.__.__k.indexOf(e) + 1) : null;
                for (var r; t < e.__k.length; t++)
                    if (null != (r = e.__k[t]) && null != r.__e)
                        return r.__e;
                return "function" == typeof e.type ? b(e) : null
            }
            function g(e) {
                var t, r;
                if (null != (e = e.__) && null != e.__c) {
                    for (e.__e = e.__c.base = null,
                    t = 0; t < e.__k.length; t++)
                        if (null != (r = e.__k[t]) && null != r.__e) {
                            e.__e = e.__c.base = r.__e;
                            break
                        }
                    return g(e)
                }
            }
            function m(e) {
                (!e.__d && (e.__d = !0) && o.push(e) && !w.__r++ || i !== t.debounceRendering) && ((i = t.debounceRendering) || a)(w)
            }
            function w() {
                var e, t, r, n, i, a, s, u;
                for (o.sort(c); e = o.shift(); )
                    e.__d && (t = o.length,
                    n = void 0,
                    i = void 0,
                    s = (a = (r = e).__v).__e,
                    (u = r.__P) && (n = [],
                    (i = f({}, a)).__v = a.__v + 1,
                    j(u, a, i, r.__n, void 0 !== u.ownerSVGElement, null != a.__h ? [s] : null, n, null == s ? b(a) : s, a.__h),
                    C(n, a),
                    a.__e != s && g(a)),
                    o.length > t && o.sort(c));
                w.__r = 0
            }
            function _(e, t, r, n, o, i, a, c, l, f) {
                var p, d, v, g, m, w, _, E = n && n.__k || u, k = E.length;
                for (r.__k = [],
                p = 0; p < t.length; p++)
                    if (null != (g = r.__k[p] = null == (g = t[p]) || "boolean" == typeof g || "function" == typeof g ? null : "string" == typeof g || "number" == typeof g || "bigint" == typeof g ? h(null, g, null, null, g) : Array.isArray(g) ? h(y, {
                        children: g
                    }, null, null, null) : g.__b > 0 ? h(g.type, g.props, g.key, g.ref ? g.ref : null, g.__v) : g)) {
                        if (g.__ = r,
                        g.__b = r.__b + 1,
                        null === (v = E[p]) || v && g.key == v.key && g.type === v.type)
                            E[p] = void 0;
                        else
                            for (d = 0; d < k; d++) {
                                if ((v = E[d]) && g.key == v.key && g.type === v.type) {
                                    E[d] = void 0;
                                    break
                                }
                                v = null
                            }
                        j(e, g, v = v || s, o, i, a, c, l, f),
                        m = g.__e,
                        (d = g.ref) && v.ref != d && (_ || (_ = []),
                        v.ref && _.push(v.ref, null, g),
                        _.push(d, g.__c || m, g)),
                        null != m ? (null == w && (w = m),
                        "function" == typeof g.type && g.__k === v.__k ? g.__d = l = O(g, l, e) : l = S(e, g, v, E, m, l),
                        "function" == typeof r.type && (r.__d = l)) : l && v.__e == l && l.parentNode != e && (l = b(v))
                    }
                for (r.__e = w,
                p = k; p--; )
                    null != E[p] && ("function" == typeof r.type && null != E[p].__e && E[p].__e == r.__d && (r.__d = P(n).nextSibling),
                    T(E[p], E[p]));
                if (_)
                    for (p = 0; p < _.length; p++)
                        I(_[p], _[++p], _[++p])
            }
            function O(e, t, r) {
                for (var n, o = e.__k, i = 0; o && i < o.length; i++)
                    (n = o[i]) && (n.__ = e,
                    t = "function" == typeof n.type ? O(n, t, r) : S(r, n, n, o, n.__e, t));
                return t
            }
            function S(e, t, r, n, o, i) {
                var a, c, s;
                if (void 0 !== t.__d)
                    a = t.__d,
                    t.__d = void 0;
                else if (null == r || o != i || null == o.parentNode)
                    e: if (null == i || i.parentNode !== e)
                        e.appendChild(o),
                        a = null;
                    else {
                        for (c = i,
                        s = 0; (c = c.nextSibling) && s < n.length; s += 1)
                            if (c == o)
                                break e;
                        e.insertBefore(o, i),
                        a = i
                    }
                return void 0 !== a ? a : o.nextSibling
            }
            function P(e) {
                var t, r, n;
                if (null == e.type || "string" == typeof e.type)
                    return e.__e;
                if (e.__k)
                    for (t = e.__k.length - 1; t >= 0; t--)
                        if ((r = e.__k[t]) && (n = P(r)))
                            return n;
                return null
            }
            function E(e, t, r) {
                "-" === t[0] ? e.setProperty(t, null == r ? "" : r) : e[t] = null == r ? "" : "number" != typeof r || l.test(t) ? r : r + "px"
            }
            function k(e, t, r, n, o) {
                var i;
                e: if ("style" === t)
                    if ("string" == typeof r)
                        e.style.cssText = r;
                    else {
                        if ("string" == typeof n && (e.style.cssText = n = ""),
                        n)
                            for (t in n)
                                r && t in r || E(e.style, t, "");
                        if (r)
                            for (t in r)
                                n && r[t] === n[t] || E(e.style, t, r[t])
                    }
                else if ("o" === t[0] && "n" === t[1])
                    i = t !== (t = t.replace(/Capture$/, "")),
                    t = t.toLowerCase()in e ? t.toLowerCase().slice(2) : t.slice(2),
                    e.l || (e.l = {}),
                    e.l[t + i] = r,
                    r ? n || e.addEventListener(t, i ? x : A, i) : e.removeEventListener(t, i ? x : A, i);
                else if ("dangerouslySetInnerHTML" !== t) {
                    if (o)
                        t = t.replace(/xlink(H|:h)/, "h").replace(/sName$/, "s");
                    else if ("width" !== t && "height" !== t && "href" !== t && "list" !== t && "form" !== t && "tabIndex" !== t && "download" !== t && t in e)
                        try {
                            e[t] = null == r ? "" : r;
                            break e
                        } catch (e) {}
                    "function" == typeof r || (null == r || !1 === r && "-" !== t[4] ? e.removeAttribute(t) : e.setAttribute(t, r))
                }
            }
            function A(e) {
                return this.l[e.type + !1](t.event ? t.event(e) : e)
            }
            function x(e) {
                return this.l[e.type + !0](t.event ? t.event(e) : e)
            }
            function j(e, r, n, o, i, a, c, s, u) {
                var l, p, d, h, b, g, m, w, O, S, P, E, k, A, x, j = r.type;
                if (void 0 !== r.constructor)
                    return null;
                null != n.__h && (u = n.__h,
                s = r.__e = n.__e,
                r.__h = null,
                a = [s]),
                (l = t.__b) && l(r);
                try {
                    e: if ("function" == typeof j) {
                        if (w = r.props,
                        O = (l = j.contextType) && o[l.__c],
                        S = l ? O ? O.props.value : l.__ : o,
                        n.__c ? m = (p = r.__c = n.__c).__ = p.__E : ("prototype"in j && j.prototype.render ? r.__c = p = new j(w,S) : (r.__c = p = new v(w,S),
                        p.constructor = j,
                        p.render = D),
                        O && O.sub(p),
                        p.props = w,
                        p.state || (p.state = {}),
                        p.context = S,
                        p.__n = o,
                        d = p.__d = !0,
                        p.__h = [],
                        p._sb = []),
                        null == p.__s && (p.__s = p.state),
                        null != j.getDerivedStateFromProps && (p.__s == p.state && (p.__s = f({}, p.__s)),
                        f(p.__s, j.getDerivedStateFromProps(w, p.__s))),
                        h = p.props,
                        b = p.state,
                        p.__v = r,
                        d)
                            null == j.getDerivedStateFromProps && null != p.componentWillMount && p.componentWillMount(),
                            null != p.componentDidMount && p.__h.push(p.componentDidMount);
                        else {
                            if (null == j.getDerivedStateFromProps && w !== h && null != p.componentWillReceiveProps && p.componentWillReceiveProps(w, S),
                            !p.__e && null != p.shouldComponentUpdate && !1 === p.shouldComponentUpdate(w, p.__s, S) || r.__v === n.__v) {
                                for (r.__v !== n.__v && (p.props = w,
                                p.state = p.__s,
                                p.__d = !1),
                                p.__e = !1,
                                r.__e = n.__e,
                                r.__k = n.__k,
                                r.__k.forEach((function(e) {
                                    e && (e.__ = r)
                                }
                                )),
                                P = 0; P < p._sb.length; P++)
                                    p.__h.push(p._sb[P]);
                                p._sb = [],
                                p.__h.length && c.push(p);
                                break e
                            }
                            null != p.componentWillUpdate && p.componentWillUpdate(w, p.__s, S),
                            null != p.componentDidUpdate && p.__h.push((function() {
                                p.componentDidUpdate(h, b, g)
                            }
                            ))
                        }
                        if (p.context = S,
                        p.props = w,
                        p.__P = e,
                        E = t.__r,
                        k = 0,
                        "prototype"in j && j.prototype.render) {
                            for (p.state = p.__s,
                            p.__d = !1,
                            E && E(r),
                            l = p.render(p.props, p.state, p.context),
                            A = 0; A < p._sb.length; A++)
                                p.__h.push(p._sb[A]);
                            p._sb = []
                        } else
                            do {
                                p.__d = !1,
                                E && E(r),
                                l = p.render(p.props, p.state, p.context),
                                p.state = p.__s
                            } while (p.__d && ++k < 25);
                        p.state = p.__s,
                        null != p.getChildContext && (o = f(f({}, o), p.getChildContext())),
                        d || null == p.getSnapshotBeforeUpdate || (g = p.getSnapshotBeforeUpdate(h, b)),
                        x = null != l && l.type === y && null == l.key ? l.props.children : l,
                        _(e, Array.isArray(x) ? x : [x], r, n, o, i, a, c, s, u),
                        p.base = r.__e,
                        r.__h = null,
                        p.__h.length && c.push(p),
                        m && (p.__E = p.__ = null),
                        p.__e = !1
                    } else
                        null == a && r.__v === n.__v ? (r.__k = n.__k,
                        r.__e = n.__e) : r.__e = R(n.__e, r, n, o, i, a, c, u);
                    (l = t.diffed) && l(r)
                } catch (e) {
                    r.__v = null,
                    (u || null != a) && (r.__e = s,
                    r.__h = !!u,
                    a[a.indexOf(s)] = null),
                    t.__e(e, r, n)
                }
            }
            function C(e, r) {
                t.__c && t.__c(r, e),
                e.some((function(r) {
                    try {
                        e = r.__h,
                        r.__h = [],
                        e.some((function(e) {
                            e.call(r)
                        }
                        ))
                    } catch (e) {
                        t.__e(e, r.__v)
                    }
                }
                ))
            }
            function R(t, r, n, o, i, a, c, u) {
                var l, f, d, h = n.props, y = r.props, v = r.type, g = 0;
                if ("svg" === v && (i = !0),
                null != a)
                    for (; g < a.length; g++)
                        if ((l = a[g]) && "setAttribute"in l == !!v && (v ? l.localName === v : 3 === l.nodeType)) {
                            t = l,
                            a[g] = null;
                            break
                        }
                if (null == t) {
                    if (null === v)
                        return document.createTextNode(y);
                    t = i ? document.createElementNS("http://www.w3.org/2000/svg", v) : document.createElement(v, y.is && y),
                    a = null,
                    u = !1
                }
                if (null === v)
                    h === y || u && t.data === y || (t.data = y);
                else {
                    if (a = a && e.call(t.childNodes),
                    f = (h = n.props || s).dangerouslySetInnerHTML,
                    d = y.dangerouslySetInnerHTML,
                    !u) {
                        if (null != a)
                            for (h = {},
                            g = 0; g < t.attributes.length; g++)
                                h[t.attributes[g].name] = t.attributes[g].value;
                        (d || f) && (d && (f && d.__html == f.__html || d.__html === t.innerHTML) || (t.innerHTML = d && d.__html || ""))
                    }
                    if (function(e, t, r, n, o) {
                        var i;
                        for (i in r)
                            "children" === i || "key" === i || i in t || k(e, i, null, r[i], n);
                        for (i in t)
                            o && "function" != typeof t[i] || "children" === i || "key" === i || "value" === i || "checked" === i || r[i] === t[i] || k(e, i, t[i], r[i], n)
                    }(t, y, h, i, u),
                    d)
                        r.__k = [];
                    else if (g = r.props.children,
                    _(t, Array.isArray(g) ? g : [g], r, n, o, i && "foreignObject" !== v, a, c, a ? a[0] : n.__k && b(n, 0), u),
                    null != a)
                        for (g = a.length; g--; )
                            null != a[g] && p(a[g]);
                    u || ("value"in y && void 0 !== (g = y.value) && (g !== t.value || "progress" === v && !g || "option" === v && g !== h.value) && k(t, "value", g, h.value, !1),
                    "checked"in y && void 0 !== (g = y.checked) && g !== t.checked && k(t, "checked", g, h.checked, !1))
                }
                return t
            }
            function I(e, r, n) {
                try {
                    "function" == typeof e ? e(r) : e.current = r
                } catch (e) {
                    t.__e(e, n)
                }
            }
            function T(e, r, n) {
                var o, i;
                if (t.unmount && t.unmount(e),
                (o = e.ref) && (o.current && o.current !== e.__e || I(o, null, r)),
                null != (o = e.__c)) {
                    if (o.componentWillUnmount)
                        try {
                            o.componentWillUnmount()
                        } catch (e) {
                            t.__e(e, r)
                        }
                    o.base = o.__P = null,
                    e.__c = void 0
                }
                if (o = e.__k)
                    for (i = 0; i < o.length; i++)
                        o[i] && T(o[i], r, n || "function" != typeof e.type);
                n || null == e.__e || p(e.__e),
                e.__ = e.__e = e.__d = void 0
            }
            function D(e, t, r) {
                return this.constructor(e, r)
            }
            function K(r, n, o) {
                var i, a, c;
                t.__ && t.__(r, n),
                a = (i = "function" == typeof o) ? null : o && o.__k || n.__k,
                c = [],
                j(n, r = (!i && o || n).__k = d(y, null, [r]), a || s, s, void 0 !== n.ownerSVGElement, !i && o ? [o] : a ? null : n.firstChild ? e.call(n.childNodes) : null, c, !i && o ? o : a ? a.__e : n.firstChild, i),
                C(c, r)
            }
            e = u.slice,
            t = {
                __e: function(e, t, r, n) {
                    for (var o, i, a; t = t.__; )
                        if ((o = t.__c) && !o.__)
                            try {
                                if ((i = o.constructor) && null != i.getDerivedStateFromError && (o.setState(i.getDerivedStateFromError(e)),
                                a = o.__d),
                                null != o.componentDidCatch && (o.componentDidCatch(e, n || {}),
                                a = o.__d),
                                a)
                                    return o.__E = o
                            } catch (t) {
                                e = t
                            }
                    throw e
                }
            },
            n = 0,
            v.prototype.setState = function(e, t) {
                var r;
                r = null != this.__s && this.__s !== this.state ? this.__s : this.__s = f({}, this.state),
                "function" == typeof e && (e = e(f({}, r), this.props)),
                e && f(r, e),
                null != e && this.__v && (t && this._sb.push(t),
                m(this))
            }
            ,
            v.prototype.forceUpdate = function(e) {
                this.__v && (this.__e = !0,
                e && this.__h.push(e),
                m(this))
            }
            ,
            v.prototype.render = y,
            o = [],
            a = "function" == typeof Promise ? Promise.prototype.then.bind(Promise.resolve()) : setTimeout,
            c = function(e, t) {
                return e.__v.__b - t.__v.__b
            }
            ,
            w.__r = 0;
            window.console && window.console.error && window.console.error.bind(window.console),
            window.console && window.console.info && window.console.info.bind(window.console),
            window.console && window.console.log && window.console.log.bind(window.console);
            var F, M = window.console && window.console.warn && window.console.warn.bind(window.console), H = function(e, t) {
                var r = e
                  , n = t.slice()
                  , o = ""
                  , i = !1
                  , a = "card" === r
                  , c = a && 1 === n.length;
                return a && !c || (c && (r = n[0]),
                n = [r],
                o = r,
                i = !0),
                {
                    cardGroupTypes: n,
                    cardBrand: o,
                    isSingleBrandedCard: i
                }
            }, U = function(e, t) {
                if (e)
                    return e.querySelector(t)
            }, L = function(e, t, r, n) {
                if ("function" != typeof e.addEventListener) {
                    if (!e.attachEvent)
                        throw new Error(": Unable to bind ".concat(t, "-event"));
                    e.attachEvent("on".concat(t), r)
                } else
                    e.addEventListener(t, r, n)
            }, N = function(e, t, r, n) {
                if ("function" == typeof e.addEventListener)
                    e.removeEventListener(t, r, n);
                else {
                    if (!e.attachEvent)
                        throw new Error(": Unable to unbind ".concat(t, "-event"));
                    e.detachEvent("on".concat(t), r)
                }
            };
            function W(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            var V = "encryptedExpiryDate"
              , B = "encryptedExpiryMonth"
              , G = "encryptedExpiryYear"
              , J = "encryptedSecurityCode"
              , z = "encryptedSecurityCode3digits"
              , Y = "encryptedSecurityCode4digits"
              , $ = "expiryMonth"
              , q = "expiryYear"
              , X = "/"
              , Q = 30
              , Z = "message blocked: event origin does not match permitted origin"
              , ee = "message blocked: postMessage data type is incorrect (event.data not present or not a string)"
              , te = "message blocked: postMessage data is not JSON"
              , re = "config message received and handled"
              , ne = "config message rejected no adyen window object"
              , oe = "config message rejected no encryption key"
              , ie = "special message received and handled"
              , ae = "special message data lacks main props"
              , ce = "special message data numKey incorrect"
              , se = "message received but not handled"
              , ue = "touch"
              , le = "focus"
              , fe = "IEClearedField"
              , pe = "KeyPressed"
              , de = "rightClickPaste"
              , he = "abcdefghijklmnopqrstuvwxyz"
              , ye = "thyquickbrownfoxjumpsoverlazydog"
              , ve = "required"
              , be = "hidden"
              , ge = ve
              , me = "error.va.gen.01"
              , we = "error.va.sf-cc-num.03"
              , _e = "RSA-OAEP"
              , Oe = (W(F = {}, "encryptedCardNumber", "error.va.sf-cc-num.04"),
            W(F, V, "error.va.sf-cc-dat.05"),
            W(F, G, "error.va.sf-cc-yr.02"),
            W(F, J, "error.va.sf-cc-cvc.02"),
            W(F, "encryptedBankAccountNumber", "error.va.sf-ach-num.02"),
            W(F, "encryptedBankLocationId", "error.va.sf-ach-loc.02"),
            W(F, "encryptedPassword", "error.va.sf-kcp-pwd.02"),
            W(F, "encryptedDigits", me),
            F)
              , Se = ["error.va.sf-cc-num.02", "error.va.sf-cc-dat.04", "error.va.sf-cc-yr.01", "error.va.sf-cc-mth.01", "error.va.sf-cc-cvc.01", "error.va.sf-kcp-pwd.01", "error.va.sf-ach-num.01", "error.va.sf-ach-loc.01", me]
              , Pe = "123456789012345678901234567890"
              , Ee = {
                base: {
                    color: "#00112C",
                    background: "#fff",
                    fontSize: "16px",
                    fontWeight: "400"
                },
                placeholder: {
                    fontWeight: "200"
                },
                error: {
                    color: "#00112c"
                },
                validated: {}
            };
            function ke(e) {
                return ke = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                ke(e)
            }
            function Ae(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function xe(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Ae(Object(r), !0).forEach((function(t) {
                        je(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Ae(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function je(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            var Ce, Re = {
                background: "background",
                caretColor: "caret-color",
                color: "color",
                display: "display",
                font: "font",
                fontFamily: "font-family",
                fontSize: "font-size",
                fontSizeAdjust: "font-size-adjust",
                fontSmoothing: "font-smoothing",
                fontStretch: "font-stretch",
                fontStyle: "font-style",
                fontVariant: "font-variant",
                fontVariantAlternates: "font-variant-alternates",
                fontVariantCaps: "font-variant-caps",
                fontVariantEastAsian: "font-variant-east-asian",
                fontVariantLigatures: "font-variant-ligatures",
                fontVariantNumeric: "font-variant-numeric",
                fontWeight: "font-weight",
                letterSpacing: "letter-spacing",
                lineHeight: "line-height",
                mozOsxFontSmoothing: "-moz-osx-font-smoothing",
                mozTransition: "moz-transition",
                outline: "outline",
                opacity: "opacity",
                padding: "padding",
                textAlign: "text-align",
                textShadow: "text-shadow",
                transition: "transition",
                webkitFontSmoothing: "-webkit-font-smoothing",
                webkitTransition: "webkit-transition",
                wordSpacing: "word-spacing"
            }, Ie = {
                base: ".input-field",
                autofill: {
                    0: ".input-field:-webkit-autofill",
                    1: ".input-field:-webkit-autofill:active",
                    2: ".input-field:-webkit-autofill:hover",
                    3: ".input-field:-webkit-autofill:focus",
                    4: ".input-field:-webkit-autofill:autofill"
                },
                error: ".chckt-input-field--error",
                validated: ".chckt-input-field--validated",
                placeholder: {
                    0: ".input-field::placeholder",
                    1: ".input-field::-webkit-input-placeholder",
                    2: ".input-field:placeholder-shown"
                },
                "::msclear": {
                    0: ".input-field::ms-clear"
                }
            }, Te = function(e) {
                return !function(e) {
                    var t = /(http|ftp|https):\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?/
                      , r = !1;
                    for (var n in e)
                        if (e.hasOwnProperty(n)) {
                            var o = e[n];
                            if (o)
                                for (var i in o)
                                    if (o.hasOwnProperty(i)) {
                                        var a = o[i];
                                        !0 === t.test(a) && (r = !0)
                                    }
                        }
                    return !0 === r
                }(e)
            }, De = function(e, t) {
                var r = t.property
                  , n = t.value;
                if ("autofill" !== e)
                    return r + ":" + n + ";";
                var o = "";
                return r === Re.background && (o = "box-shadow: 0 0 0 1000px ".concat(n, " inset !important;background-color:").concat(n, " !important;")),
                r === Re.color && (o = "-webkit-text-fill-color: ".concat(n, ";color:").concat(n, " !important;")),
                o
            }, Ke = function(e) {
                return function(t) {
                    for (var r = xe(xe({}, t), {}, {
                        autofill: xe({}, t.base)
                    }), n = Object.keys(r), o = 0; o < n.length; o++) {
                        var i = n[o]
                          , a = []
                          , c = Object.keys(r[i])
                          , s = [];
                        for (var u in r[i])
                            r[i].hasOwnProperty(u) && s.push(r[i][u]);
                        for (var l = 0; l < c.length; l++) {
                            var f = c[l]
                              , p = s[l]
                              , d = Re[f];
                            if (d) {
                                var h = De(i, {
                                    property: d,
                                    value: p
                                });
                                a.push(h)
                            }
                        }
                        if (Ie[i] && a) {
                            var y = a.filter(Boolean).join("");
                            e(y, Ie[i], i)
                        }
                    }
                }
            }, Fe = function(e) {
                var t = document.createElement("style");
                return t.setAttribute("data-styling-key", e),
                t.appendChild(document.createTextNode("")),
                document.head.appendChild(t),
                t.sheet
            }, Me = function(e, t, r) {
                try {
                    if ("object" === ke(t))
                        for (var n in t)
                            t[n] && e.insertRule && e.insertRule(t[n] + " {" + r + "}", 0);
                    else
                        e.insertRule && e.insertRule(t + "{" + r + "}", 0)
                } catch (e) {}
            }, He = Ke((function(e, t, r) {
                var n = Fe(r);
                Me(n, t, e)
            }
            )), Ue = Ke((function(e, t, r) {
                var n = Le(r);
                n ? Ne(n) : n = Fe(r),
                Me(n, t, e)
            }
            )), Le = function(e) {
                var t = U(document, '[data-styling-key="' + e + '"]');
                return t ? t.sheet : null
            }, Ne = function(e) {
                for (var t = e.cssRules.length, r = 0; r < t; r++)
                    e.deleteRule(0)
            };
            const We = {
                process: function() {
                    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
                      , t = {
                        base: xe(xe({}, Ee.base), e.base),
                        placeholder: xe(xe({}, Ee.placeholder), e.placeholder),
                        validated: xe(xe({}, Ee.validated), e.validated),
                        error: xe(xe({}, Ee.error), e.error)
                    };
                    Ce = Te(t) ? t : xe({}, Ee),
                    He(Ce)
                },
                update: function(e) {
                    var t = {
                        base: xe(xe({}, Ce.base), e.base),
                        placeholder: xe(xe({}, Ce.placeholder), e.placeholder),
                        validated: xe(xe({}, Ce.validated), e.validated),
                        error: xe(xe({}, Ce.error), e.error)
                    };
                    Te(t) && Ue(Ce = t)
                }
            };
            function Ve(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return Be(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return Be(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return Be(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function Be(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function Ge(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Je(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Ge(Object(r), !0).forEach((function(t) {
                        ze(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Ge(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function ze(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Ye(e) {
                return Ye = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                Ye(e)
            }
            function $e(e) {
                return "object" === Ye(e) && null !== e && "[object Array]" === Object.prototype.toString.call(e)
            }
            function qe(e, t) {
                return t.split(".").reduce((function(e, t) {
                    return e && e[t] ? e[t] : void 0
                }
                ), e)
            }
            function Xe(e, t, r) {
                return Je(Je({}, e), {}, ze({}, t, r))
            }
            function Qe(e, t) {
                var r = e && Object.keys(e);
                r && r.length && r.map((function(r) {
                    return t[r] = e[r],
                    !0
                }
                ))
            }
            function Ze() {
                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                    t[r] = arguments[r];
                var n = $e(t[0]) ? t[0] : t;
                return {
                    from: function(e) {
                        return n.map((function(t) {
                            return t in e ? ze({}, t, e[t]) : {}
                        }
                        )).reduce((function(e, t) {
                            return Je(Je({}, e), t)
                        }
                        ), {})
                    }
                }
            }
            function et() {
                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                    t[r] = arguments[r];
                var n = $e(t[0]) ? t[0] : t;
                return {
                    from: function(e) {
                        var t = Object.keys(e).filter((function(e) {
                            return !n.includes(e)
                        }
                        ));
                        return Ze.apply(void 0, Ve(t)).from(e)
                    }
                }
            }
            const tt = crypto;
            var rt = function(e) {
                return e instanceof CryptoKey
            };
            function nt(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            var ot = function() {
                var e, t = (e = regeneratorRuntime.mark((function e(t, r) {
                    var n;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return n = "SHA-".concat(t.slice(-3)),
                                e.t0 = Uint8Array,
                                e.next = 4,
                                tt.subtle.digest(n, r);
                            case 4:
                                return e.t1 = e.sent,
                                e.abrupt("return", new e.t0(e.t1));
                            case 6:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            nt(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            nt(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                );
                return function(e, r) {
                    return t.apply(this, arguments)
                }
            }();
            const it = ot;
            function at(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            var ct = new TextEncoder
              , st = new TextDecoder
              , ut = Math.pow(2, 32);
            function lt() {
                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                    t[r] = arguments[r];
                var n = t.reduce((function(e, t) {
                    return e + t.length
                }
                ), 0)
                  , o = new Uint8Array(n)
                  , i = 0;
                return t.forEach((function(e) {
                    o.set(e, i),
                    i += e.length
                }
                )),
                o
            }
            function ft(e, t) {
                return lt(ct.encode(e), new Uint8Array([0]), t)
            }
            function pt(e, t, r) {
                if (t < 0 || t >= ut)
                    throw new RangeError("value must be >= 0 and <= ".concat(ut - 1, ". Received ").concat(t));
                e.set([t >>> 24, t >>> 16, t >>> 8, 255 & t], r)
            }
            function dt(e) {
                var t = new Uint8Array(4);
                return pt(t, e),
                t
            }
            function ht(e) {
                return lt(dt(e.length), e)
            }
            function yt(e, t, r) {
                return vt.apply(this, arguments)
            }
            function vt() {
                var e;
                return e = regeneratorRuntime.mark((function e(t, r, n) {
                    var o, i, a, c;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                o = Math.ceil((r >> 3) / 32),
                                i = new Uint8Array(32 * o),
                                a = 0;
                            case 3:
                                if (!(a < o)) {
                                    e.next = 17;
                                    break
                                }
                                return (c = new Uint8Array(4 + t.length + n.length)).set(dt(a + 1)),
                                c.set(t, 4),
                                c.set(n, 4 + t.length),
                                e.t0 = i,
                                e.next = 11,
                                it("sha256", c);
                            case 11:
                                e.t1 = e.sent,
                                e.t2 = 32 * a,
                                e.t0.set.call(e.t0, e.t1, e.t2);
                            case 14:
                                a++,
                                e.next = 3;
                                break;
                            case 17:
                                return e.abrupt("return", i.slice(0, r >> 3));
                            case 18:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                vt = function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            at(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            at(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                ,
                vt.apply(this, arguments)
            }
            var bt = function(e) {
                return function(e) {
                    var t = e;
                    "string" == typeof t && (t = ct.encode(t));
                    for (var r = [], n = 0; n < t.length; n += 32768)
                        r.push(String.fromCharCode.apply(null, t.subarray(n, n + 32768)));
                    return btoa(r.join(""))
                }(e).replace(/=/g, "").replace(/\+/g, "-").replace(/\//g, "_")
            }
              , gt = function(e) {
                var t = e;
                t instanceof Uint8Array && (t = st.decode(t)),
                t = t.replace(/-/g, "+").replace(/_/g, "/").replace(/\s/g, "");
                try {
                    return function(e) {
                        for (var t = atob(e), r = new Uint8Array(t.length), n = 0; n < t.length; n++)
                            r[n] = t.charCodeAt(n);
                        return r
                    }(t)
                } catch (e) {
                    throw new TypeError("The input to be decoded is not correctly encoded.")
                }
            };
            function mt(e) {
                return mt = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                mt(e)
            }
            function wt(e, t) {
                if (!(e instanceof t))
                    throw new TypeError("Cannot call a class as a function")
            }
            function _t(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            function Ot(e, t, r) {
                return t && _t(e.prototype, t),
                r && _t(e, r),
                Object.defineProperty(e, "prototype", {
                    writable: !1
                }),
                e
            }
            function St(e, t) {
                if ("function" != typeof t && null !== t)
                    throw new TypeError("Super expression must either be null or a function");
                e.prototype = Object.create(t && t.prototype, {
                    constructor: {
                        value: e,
                        writable: !0,
                        configurable: !0
                    }
                }),
                Object.defineProperty(e, "prototype", {
                    writable: !1
                }),
                t && jt(e, t)
            }
            function Pt(e) {
                var t = xt();
                return function() {
                    var r, n = Ct(e);
                    if (t) {
                        var o = Ct(this).constructor;
                        r = Reflect.construct(n, arguments, o)
                    } else
                        r = n.apply(this, arguments);
                    return function(e, t) {
                        if (t && ("object" === mt(t) || "function" == typeof t))
                            return t;
                        if (void 0 !== t)
                            throw new TypeError("Derived constructors may only return object or undefined");
                        return Et(e)
                    }(this, r)
                }
            }
            function Et(e) {
                if (void 0 === e)
                    throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                return e
            }
            function kt(e) {
                var t = "function" == typeof Map ? new Map : void 0;
                return kt = function(e) {
                    if (null === e || (r = e,
                    -1 === Function.toString.call(r).indexOf("[native code]")))
                        return e;
                    var r;
                    if ("function" != typeof e)
                        throw new TypeError("Super expression must either be null or a function");
                    if (void 0 !== t) {
                        if (t.has(e))
                            return t.get(e);
                        t.set(e, n)
                    }
                    function n() {
                        return At(e, arguments, Ct(this).constructor)
                    }
                    return n.prototype = Object.create(e.prototype, {
                        constructor: {
                            value: n,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    jt(n, e)
                }
                ,
                kt(e)
            }
            function At(e, t, r) {
                return At = xt() ? Reflect.construct.bind() : function(e, t, r) {
                    var n = [null];
                    n.push.apply(n, t);
                    var o = new (Function.bind.apply(e, n));
                    return r && jt(o, r.prototype),
                    o
                }
                ,
                At.apply(null, arguments)
            }
            function xt() {
                if ("undefined" == typeof Reflect || !Reflect.construct)
                    return !1;
                if (Reflect.construct.sham)
                    return !1;
                if ("function" == typeof Proxy)
                    return !0;
                try {
                    return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}
                    ))),
                    !0
                } catch (e) {
                    return !1
                }
            }
            function jt(e, t) {
                return jt = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                    return e.__proto__ = t,
                    e
                }
                ,
                jt(e, t)
            }
            function Ct(e) {
                return Ct = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                    return e.__proto__ || Object.getPrototypeOf(e)
                }
                ,
                Ct(e)
            }
            var Rt = function(e) {
                St(r, e);
                var t = Pt(r);
                function r(e) {
                    var n, o;
                    return wt(this, r),
                    (n = t.call(this, e)).code = "ERR_JOSE_GENERIC",
                    n.name = n.constructor.name,
                    null === (o = Error.captureStackTrace) || void 0 === o || o.call(Error, Et(n), n.constructor),
                    n
                }
                return Ot(r, null, [{
                    key: "code",
                    get: function() {
                        return "ERR_JOSE_GENERIC"
                    }
                }]),
                r
            }(kt(Error))
              , It = function(e) {
                St(r, e);
                var t = Pt(r);
                function r() {
                    var e;
                    return wt(this, r),
                    (e = t.apply(this, arguments)).code = "ERR_JOSE_NOT_SUPPORTED",
                    e
                }
                return Ot(r, null, [{
                    key: "code",
                    get: function() {
                        return "ERR_JOSE_NOT_SUPPORTED"
                    }
                }]),
                r
            }(Rt)
              , Tt = function(e) {
                St(r, e);
                var t = Pt(r);
                function r() {
                    var e;
                    return wt(this, r),
                    (e = t.apply(this, arguments)).code = "ERR_JWE_INVALID",
                    e
                }
                return Ot(r, null, [{
                    key: "code",
                    get: function() {
                        return "ERR_JWE_INVALID"
                    }
                }]),
                r
            }(Rt);
            Symbol.asyncIterator;
            const Dt = tt.getRandomValues.bind(tt);
            function Kt(e) {
                switch (e) {
                case "A128GCM":
                case "A128GCMKW":
                case "A192GCM":
                case "A192GCMKW":
                case "A256GCM":
                case "A256GCMKW":
                    return 96;
                case "A128CBC-HS256":
                case "A192CBC-HS384":
                case "A256CBC-HS512":
                    return 128;
                default:
                    throw new It("Unsupported JWE Algorithm: ".concat(e))
                }
            }
            const Ft = function(e) {
                return Dt(new Uint8Array(Kt(e) >> 3))
            };
            const Mt = function(e, t) {
                if (t.length << 3 !== Kt(e))
                    throw new Tt("Invalid Initialization Vector length")
            };
            const Ht = function(e, t) {
                var r = e.byteLength << 3;
                if (r !== t)
                    throw new Tt("Invalid Content Encryption Key length. Expected ".concat(t, " bits, got ").concat(r, " bits"))
            }
              , Ut = function(e) {
                return rt(e)
            };
            var Lt = ["CryptoKey"];
            function Nt(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Wt(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            Nt(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            Nt(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            var Vt = function() {
                var e = Wt(regeneratorRuntime.mark((function e() {
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                throw new It('JWE "zip" (Compression Algorithm) Header Parameter is not supported by your javascript runtime. You need to use the `deflateRaw` encrypt option to provide Deflate Raw implementation.');
                            case 1:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function() {
                    return e.apply(this, arguments)
                }
            }();
            const Bt = [{
                hash: "SHA-256",
                name: "HMAC"
            }, !0, ["sign"]];
            function Gt(e) {
                return new TypeError("CryptoKey does not support this operation, its ".concat(arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "algorithm.name", " must be ").concat(e))
            }
            function Jt(e, t) {
                return e.name === t
            }
            function zt(e) {
                return parseInt(e.name.slice(4), 10)
            }
            function Yt(e, t) {
                if (t.length && !t.some((function(t) {
                    return e.usages.includes(t)
                }
                ))) {
                    var r = "CryptoKey does not support this operation, its usages must include ";
                    if (t.length > 2) {
                        var n = t.pop();
                        r += "one of ".concat(t.join(", "), ", or ").concat(n, ".")
                    } else
                        2 === t.length ? r += "one of ".concat(t[0], " or ").concat(t[1], ".") : r += "".concat(t[0], ".");
                    throw new TypeError(r)
                }
            }
            function $t(e, t) {
                switch (t) {
                case "A128GCM":
                case "A192GCM":
                case "A256GCM":
                    if (!Jt(e.algorithm, "AES-GCM"))
                        throw Gt("AES-GCM");
                    var r = parseInt(t.slice(1, 4), 10);
                    if (e.algorithm.length !== r)
                        throw Gt(r, "algorithm.length");
                    break;
                case "A128KW":
                case "A192KW":
                case "A256KW":
                    if (!Jt(e.algorithm, "AES-KW"))
                        throw Gt("AES-KW");
                    var n = parseInt(t.slice(1, 4), 10);
                    if (e.algorithm.length !== n)
                        throw Gt(n, "algorithm.length");
                    break;
                case "ECDH":
                    switch (e.algorithm.name) {
                    case "ECDH":
                    case "X25519":
                    case "X448":
                        break;
                    default:
                        throw Gt("ECDH, X25519, or X448")
                    }
                    break;
                case "PBES2-HS256+A128KW":
                case "PBES2-HS384+A192KW":
                case "PBES2-HS512+A256KW":
                    if (!Jt(e.algorithm, "PBKDF2"))
                        throw Gt("PBKDF2");
                    break;
                case "RSA-OAEP":
                case "RSA-OAEP-256":
                case "RSA-OAEP-384":
                case "RSA-OAEP-512":
                    if (!Jt(e.algorithm, "RSA-OAEP"))
                        throw Gt("RSA-OAEP");
                    var o = parseInt(t.slice(9), 10) || 1;
                    if (zt(e.algorithm.hash) !== o)
                        throw Gt("SHA-".concat(o), "algorithm.hash");
                    break;
                default:
                    throw new TypeError("CryptoKey does not support this operation")
                }
                for (var i = arguments.length, a = new Array(i > 2 ? i - 2 : 0), c = 2; c < i; c++)
                    a[c - 2] = arguments[c];
                Yt(e, a)
            }
            function qt(e) {
                return qt = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                qt(e)
            }
            function Xt(e, t) {
                for (var r = arguments.length, n = new Array(r > 2 ? r - 2 : 0), o = 2; o < r; o++)
                    n[o - 2] = arguments[o];
                if (n.length > 2) {
                    var i = n.pop();
                    e += "one of type ".concat(n.join(", "), ", or ").concat(i, ".")
                } else
                    2 === n.length ? e += "one of type ".concat(n[0], " or ").concat(n[1], ".") : e += "of type ".concat(n[0], ".");
                return null == t ? e += " Received ".concat(t) : "function" == typeof t && t.name ? e += " Received function ".concat(t.name) : "object" === qt(t) && null != t && t.constructor && t.constructor.name && (e += " Received an instance of ".concat(t.constructor.name)),
                e
            }
            const Qt = function(e) {
                for (var t = arguments.length, r = new Array(t > 1 ? t - 1 : 0), n = 1; n < t; n++)
                    r[n - 1] = arguments[n];
                return Xt.apply(void 0, ["Key must be ", e].concat(r))
            };
            function Zt(e, t) {
                for (var r = arguments.length, n = new Array(r > 2 ? r - 2 : 0), o = 2; o < r; o++)
                    n[o - 2] = arguments[o];
                return Xt.apply(void 0, ["Key for the ".concat(e, " algorithm must be "), t].concat(n))
            }
            function er(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function tr(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            er(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            er(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function rr(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return nr(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return nr(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return nr(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function nr(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function or(e, t) {
                if (e.algorithm.length !== parseInt(t.slice(1, 4), 10))
                    throw new TypeError("Invalid key size for alg: ".concat(t))
            }
            function ir(e, t, r) {
                if (rt(e))
                    return $t(e, t, r),
                    e;
                if (e instanceof Uint8Array)
                    return tt.subtle.importKey("raw", e, "AES-KW", !0, [r]);
                throw new TypeError(Qt.apply(void 0, [e].concat(rr(Lt), ["Uint8Array"])))
            }
            var ar = function() {
                var e = tr(regeneratorRuntime.mark((function e(t, r, n) {
                    var o, i, a;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return e.next = 2,
                                ir(r, t, "wrapKey");
                            case 2:
                                return or(i = e.sent, t),
                                e.next = 6,
                                (o = tt.subtle).importKey.apply(o, ["raw", n].concat(rr(Bt)));
                            case 6:
                                return a = e.sent,
                                e.t0 = Uint8Array,
                                e.next = 10,
                                tt.subtle.wrapKey("raw", a, i, "AES-KW");
                            case 10:
                                return e.t1 = e.sent,
                                e.abrupt("return", new e.t0(e.t1));
                            case 12:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, r, n) {
                    return e.apply(this, arguments)
                }
            }();
            function cr(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return sr(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return sr(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return sr(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function sr(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function ur(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function lr(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            ur(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            ur(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function fr(e, t, r, n) {
                return pr.apply(this, arguments)
            }
            function pr() {
                return pr = lr(regeneratorRuntime.mark((function e(t, r, n, o) {
                    var i, a, c, s, u, l = arguments;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (i = l.length > 4 && void 0 !== l[4] ? l[4] : new Uint8Array(0),
                                a = l.length > 5 && void 0 !== l[5] ? l[5] : new Uint8Array(0),
                                rt(t)) {
                                    e.next = 4;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [t].concat(cr(Lt))));
                            case 4:
                                if ($t(t, "ECDH"),
                                rt(r)) {
                                    e.next = 7;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [r].concat(cr(Lt))));
                            case 7:
                                return $t(r, "ECDH", "deriveBits"),
                                c = lt(ht(ct.encode(n)), ht(i), ht(a), dt(o)),
                                s = "X25519" === t.algorithm.name ? 256 : "X448" === t.algorithm.name ? 448 : Math.ceil(parseInt(t.algorithm.namedCurve.substr(-3), 10) / 8) << 3,
                                e.t0 = Uint8Array,
                                e.next = 13,
                                tt.subtle.deriveBits({
                                    name: t.algorithm.name,
                                    public: t
                                }, r, s);
                            case 13:
                                return e.t1 = e.sent,
                                u = new e.t0(e.t1),
                                e.abrupt("return", yt(u, o, c));
                            case 16:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                ))),
                pr.apply(this, arguments)
            }
            function dr(e) {
                return hr.apply(this, arguments)
            }
            function hr() {
                return (hr = lr(regeneratorRuntime.mark((function e(t) {
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (rt(t)) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [t].concat(cr(Lt))));
                            case 2:
                                return e.abrupt("return", tt.subtle.generateKey(t.algorithm, !0, ["deriveBits"]));
                            case 3:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            function yr(e) {
                if (!rt(e))
                    throw new TypeError(Qt.apply(void 0, [e].concat(cr(Lt))));
                return ["P-256", "P-384", "P-521"].includes(e.algorithm.namedCurve) || "X25519" === e.algorithm.name || "X448" === e.algorithm.name
            }
            function vr(e) {
                if (!(e instanceof Uint8Array) || e.length < 8)
                    throw new Tt("PBES2 Salt Input must be 8 or more octets")
            }
            function br(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function gr(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            br(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            br(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function mr(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return wr(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return wr(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return wr(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function wr(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function _r(e, t) {
                if (e instanceof Uint8Array)
                    return tt.subtle.importKey("raw", e, "PBKDF2", !1, ["deriveBits"]);
                if (rt(e))
                    return $t(e, t, "deriveBits", "deriveKey"),
                    e;
                throw new TypeError(Qt.apply(void 0, [e].concat(mr(Lt), ["Uint8Array"])))
            }
            function Or(e, t, r, n) {
                return Sr.apply(this, arguments)
            }
            function Sr() {
                return (Sr = gr(regeneratorRuntime.mark((function e(t, r, n, o) {
                    var i, a, c, s, u;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return vr(t),
                                i = ft(r, t),
                                a = parseInt(r.slice(13, 16), 10),
                                c = {
                                    hash: "SHA-".concat(r.slice(8, 11)),
                                    iterations: n,
                                    name: "PBKDF2",
                                    salt: i
                                },
                                s = {
                                    length: a,
                                    name: "AES-KW"
                                },
                                e.next = 7,
                                _r(o, r);
                            case 7:
                                if (!(u = e.sent).usages.includes("deriveBits")) {
                                    e.next = 14;
                                    break
                                }
                                return e.t0 = Uint8Array,
                                e.next = 12,
                                tt.subtle.deriveBits(c, u, a);
                            case 12:
                                return e.t1 = e.sent,
                                e.abrupt("return", new e.t0(e.t1));
                            case 14:
                                if (!u.usages.includes("deriveKey")) {
                                    e.next = 16;
                                    break
                                }
                                return e.abrupt("return", tt.subtle.deriveKey(c, u, s, !1, ["wrapKey", "unwrapKey"]));
                            case 16:
                                throw new TypeError('PBKDF2 key "usages" must include "deriveBits" or "deriveKey"');
                            case 17:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            var Pr = function() {
                var e = gr(regeneratorRuntime.mark((function e(t, r, n) {
                    var o, i, a, c, s = arguments;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return o = s.length > 3 && void 0 !== s[3] ? s[3] : 2048,
                                i = s.length > 4 && void 0 !== s[4] ? s[4] : Dt(new Uint8Array(16)),
                                e.next = 4,
                                Or(i, t, o, r);
                            case 4:
                                return a = e.sent,
                                e.next = 7,
                                ar(t.slice(-6), a, n);
                            case 7:
                                return c = e.sent,
                                e.abrupt("return", {
                                    encryptedKey: c,
                                    p2c: o,
                                    p2s: bt(i)
                                });
                            case 9:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, r, n) {
                    return e.apply(this, arguments)
                }
            }();
            function Er(e) {
                switch (e) {
                case "RSA-OAEP":
                case "RSA-OAEP-256":
                case "RSA-OAEP-384":
                case "RSA-OAEP-512":
                    return "RSA-OAEP";
                default:
                    throw new It("alg ".concat(e, " is not supported either by JOSE or your javascript runtime"))
                }
            }
            const kr = function(e, t) {
                if (e.startsWith("RS") || e.startsWith("PS")) {
                    var r = t.algorithm.modulusLength;
                    if ("number" != typeof r || r < 2048)
                        throw new TypeError("".concat(e, " requires key modulusLength to be 2048 bits or larger"))
                }
            };
            function Ar(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return xr(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return xr(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return xr(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function xr(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function jr(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Cr(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            jr(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            jr(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            var Rr = function() {
                var e = Cr(regeneratorRuntime.mark((function e(t, r, n) {
                    var o, i;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (rt(r)) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [r].concat(Ar(Lt))));
                            case 2:
                                if ($t(r, t, "encrypt", "wrapKey"),
                                kr(t, r),
                                !r.usages.includes("encrypt")) {
                                    e.next = 10;
                                    break
                                }
                                return e.t0 = Uint8Array,
                                e.next = 8,
                                tt.subtle.encrypt(Er(t), r, n);
                            case 8:
                                return e.t1 = e.sent,
                                e.abrupt("return", new e.t0(e.t1));
                            case 10:
                                if (!r.usages.includes("wrapKey")) {
                                    e.next = 19;
                                    break
                                }
                                return e.next = 13,
                                (o = tt.subtle).importKey.apply(o, ["raw", n].concat(Ar(Bt)));
                            case 13:
                                return i = e.sent,
                                e.t2 = Uint8Array,
                                e.next = 17,
                                tt.subtle.wrapKey("raw", i, r, Er(t));
                            case 17:
                                return e.t3 = e.sent,
                                e.abrupt("return", new e.t2(e.t3));
                            case 19:
                                throw new TypeError('RSA-OAEP key "usages" must include "encrypt" or "wrapKey" for this operation');
                            case 20:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, r, n) {
                    return e.apply(this, arguments)
                }
            }();
            function Ir(e) {
                switch (e) {
                case "A128GCM":
                    return 128;
                case "A192GCM":
                    return 192;
                case "A256GCM":
                case "A128CBC-HS256":
                    return 256;
                case "A192CBC-HS384":
                    return 384;
                case "A256CBC-HS512":
                    return 512;
                default:
                    throw new It("Unsupported JWE Algorithm: ".concat(e))
                }
            }
            const Tr = function(e) {
                return Dt(new Uint8Array(Ir(e) >> 3))
            };
            function Dr(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Kr(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Dr(Object(r), !0).forEach((function(t) {
                        Fr(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Dr(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function Fr(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Mr(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Hr(e) {
                var t, r;
                switch (e.kty) {
                case "oct":
                    switch (e.alg) {
                    case "HS256":
                    case "HS384":
                    case "HS512":
                        t = {
                            name: "HMAC",
                            hash: "SHA-".concat(e.alg.slice(-3))
                        },
                        r = ["sign", "verify"];
                        break;
                    case "A128CBC-HS256":
                    case "A192CBC-HS384":
                    case "A256CBC-HS512":
                        throw new It("".concat(e.alg, " keys cannot be imported as CryptoKey instances"));
                    case "A128GCM":
                    case "A192GCM":
                    case "A256GCM":
                    case "A128GCMKW":
                    case "A192GCMKW":
                    case "A256GCMKW":
                        t = {
                            name: "AES-GCM"
                        },
                        r = ["encrypt", "decrypt"];
                        break;
                    case "A128KW":
                    case "A192KW":
                    case "A256KW":
                        t = {
                            name: "AES-KW"
                        },
                        r = ["wrapKey", "unwrapKey"];
                        break;
                    case "PBES2-HS256+A128KW":
                    case "PBES2-HS384+A192KW":
                    case "PBES2-HS512+A256KW":
                        t = {
                            name: "PBKDF2"
                        },
                        r = ["deriveBits"];
                        break;
                    default:
                        throw new It('Invalid or unsupported JWK "alg" (Algorithm) Parameter value')
                    }
                    break;
                case "RSA":
                    switch (e.alg) {
                    case "PS256":
                    case "PS384":
                    case "PS512":
                        t = {
                            name: "RSA-PSS",
                            hash: "SHA-".concat(e.alg.slice(-3))
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "RS256":
                    case "RS384":
                    case "RS512":
                        t = {
                            name: "RSASSA-PKCS1-v1_5",
                            hash: "SHA-".concat(e.alg.slice(-3))
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "RSA-OAEP":
                    case "RSA-OAEP-256":
                    case "RSA-OAEP-384":
                    case "RSA-OAEP-512":
                        t = {
                            name: "RSA-OAEP",
                            hash: "SHA-".concat(parseInt(e.alg.slice(-3), 10) || 1)
                        },
                        r = e.d ? ["decrypt", "unwrapKey"] : ["encrypt", "wrapKey"];
                        break;
                    default:
                        throw new It('Invalid or unsupported JWK "alg" (Algorithm) Parameter value')
                    }
                    break;
                case "EC":
                    switch (e.alg) {
                    case "ES256":
                        t = {
                            name: "ECDSA",
                            namedCurve: "P-256"
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "ES384":
                        t = {
                            name: "ECDSA",
                            namedCurve: "P-384"
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "ES512":
                        t = {
                            name: "ECDSA",
                            namedCurve: "P-521"
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "ECDH-ES":
                    case "ECDH-ES+A128KW":
                    case "ECDH-ES+A192KW":
                    case "ECDH-ES+A256KW":
                        t = {
                            name: "ECDH",
                            namedCurve: e.crv
                        },
                        r = e.d ? ["deriveBits"] : [];
                        break;
                    default:
                        throw new It('Invalid or unsupported JWK "alg" (Algorithm) Parameter value')
                    }
                    break;
                case "OKP":
                    switch (e.alg) {
                    case "EdDSA":
                        t = {
                            name: e.crv
                        },
                        r = e.d ? ["sign"] : ["verify"];
                        break;
                    case "ECDH-ES":
                    case "ECDH-ES+A128KW":
                    case "ECDH-ES+A192KW":
                    case "ECDH-ES+A256KW":
                        t = {
                            name: e.crv
                        },
                        r = e.d ? ["deriveBits"] : [];
                        break;
                    default:
                        throw new It('Invalid or unsupported JWK "alg" (Algorithm) Parameter value')
                    }
                    break;
                default:
                    throw new It('Invalid or unsupported JWK "kty" (Key Type) Parameter value')
                }
                return {
                    algorithm: t,
                    keyUsages: r
                }
            }
            var Ur = function() {
                var e, t = (e = regeneratorRuntime.mark((function e(t) {
                    var r, n, o, i, a, c, s, u, l;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (t.alg) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError('"alg" argument is required when "jwk.alg" is not present');
                            case 2:
                                if (i = Hr(t),
                                a = i.algorithm,
                                c = i.keyUsages,
                                s = [a, null !== (n = t.ext) && void 0 !== n && n, null !== (o = t.key_ops) && void 0 !== o ? o : c],
                                "PBKDF2" !== a.name) {
                                    e.next = 6;
                                    break
                                }
                                return e.abrupt("return", (u = tt.subtle).importKey.apply(u, ["raw", gt(t.k)].concat(s)));
                            case 6:
                                return delete (l = Kr({}, t)).alg,
                                delete l.use,
                                e.abrupt("return", (r = tt.subtle).importKey.apply(r, ["jwk", l].concat(s)));
                            case 10:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            Mr(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            Mr(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                );
                return function(e) {
                    return t.apply(this, arguments)
                }
            }();
            const Lr = Ur;
            function Nr(e) {
                return Nr = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                Nr(e)
            }
            function Wr(e) {
                if ("object" !== Nr(t = e) || null === t || "[object Object]" !== Object.prototype.toString.call(e))
                    return !1;
                var t;
                if (null === Object.getPrototypeOf(e))
                    return !0;
                for (var r = e; null !== Object.getPrototypeOf(r); )
                    r = Object.getPrototypeOf(r);
                return Object.getPrototypeOf(e) === r
            }
            function Vr(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Br(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Vr(Object(r), !0).forEach((function(t) {
                        Gr(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Vr(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function Gr(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Jr(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function zr(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            Jr(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            Jr(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function Yr(e, t, r) {
                return $r.apply(this, arguments)
            }
            function $r() {
                return ($r = zr(regeneratorRuntime.mark((function e(t, r, n) {
                    var o;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (Wr(t)) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError("JWK must be an object");
                            case 2:
                                r || (r = t.alg),
                                e.t0 = t.kty,
                                e.next = "oct" === e.t0 ? 6 : "RSA" === e.t0 ? 12 : "EC" === e.t0 || "OKP" === e.t0 ? 14 : 15;
                                break;
                            case 6:
                                if ("string" == typeof t.k && t.k) {
                                    e.next = 8;
                                    break
                                }
                                throw new TypeError('missing "k" (Key Value) Parameter value');
                            case 8:
                                if (null != n || (n = !0 !== t.ext),
                                !n) {
                                    e.next = 11;
                                    break
                                }
                                return e.abrupt("return", Lr(Br(Br({}, t), {}, {
                                    alg: r,
                                    ext: null !== (o = t.ext) && void 0 !== o && o
                                })));
                            case 11:
                                return e.abrupt("return", gt(t.k));
                            case 12:
                                if (void 0 === t.oth) {
                                    e.next = 14;
                                    break
                                }
                                throw new It('RSA JWK "oth" (Other Primes Info) Parameter value is not supported');
                            case 14:
                                return e.abrupt("return", Lr(Br(Br({}, t), {}, {
                                    alg: r
                                })));
                            case 15:
                                throw new It('Unsupported "kty" (Key Type) Parameter value');
                            case 16:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            function qr(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return Xr(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return Xr(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return Xr(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function Xr(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            const Qr = function(e, t, r) {
                e.startsWith("HS") || "dir" === e || e.startsWith("PBES2") || /^A\d{3}(?:GCM)?KW$/.test(e) ? function(e, t) {
                    if (!(t instanceof Uint8Array)) {
                        if (!Ut(t))
                            throw new TypeError(Zt.apply(void 0, [e, t].concat(qr(Lt), ["Uint8Array"])));
                        if ("secret" !== t.type)
                            throw new TypeError("".concat(Lt.join(" or "), ' instances for symmetric algorithms must be of type "secret"'))
                    }
                }(e, t) : function(e, t, r) {
                    if (!Ut(t))
                        throw new TypeError(Zt.apply(void 0, [e, t].concat(qr(Lt))));
                    if ("secret" === t.type)
                        throw new TypeError("".concat(Lt.join(" or "), ' instances for asymmetric algorithms must not be of type "secret"'));
                    if ("sign" === r && "public" === t.type)
                        throw new TypeError("".concat(Lt.join(" or "), ' instances for asymmetric algorithm signing must be of type "private"'));
                    if ("decrypt" === r && "public" === t.type)
                        throw new TypeError("".concat(Lt.join(" or "), ' instances for asymmetric algorithm decryption must be of type "private"'));
                    if (t.algorithm && "verify" === r && "private" === t.type)
                        throw new TypeError("".concat(Lt.join(" or "), ' instances for asymmetric algorithm verifying must be of type "public"'));
                    if (t.algorithm && "encrypt" === r && "private" === t.type)
                        throw new TypeError("".concat(Lt.join(" or "), ' instances for asymmetric algorithm encryption must be of type "public"'))
                }(e, t, r)
            };
            function Zr(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return en(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return en(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return en(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function en(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function tn(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function rn(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            tn(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            tn(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function nn(e, t, r, n, o) {
                return on.apply(this, arguments)
            }
            function on() {
                return (on = rn(regeneratorRuntime.mark((function e(t, r, n, o, i) {
                    var a, c, s, u, l, f;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (n instanceof Uint8Array) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError(Qt(n, "Uint8Array"));
                            case 2:
                                return a = parseInt(t.slice(1, 4), 10),
                                e.next = 5,
                                tt.subtle.importKey("raw", n.subarray(a >> 3), "AES-CBC", !1, ["encrypt"]);
                            case 5:
                                return c = e.sent,
                                e.next = 8,
                                tt.subtle.importKey("raw", n.subarray(0, a >> 3), {
                                    hash: "SHA-".concat(a << 1),
                                    name: "HMAC"
                                }, !1, ["sign"]);
                            case 8:
                                return s = e.sent,
                                e.t0 = Uint8Array,
                                e.next = 12,
                                tt.subtle.encrypt({
                                    iv: o,
                                    name: "AES-CBC"
                                }, c, r);
                            case 12:
                                return e.t1 = e.sent,
                                u = new e.t0(e.t1),
                                l = lt(i, o, u, (p = i.length << 3,
                                d = void 0,
                                h = void 0,
                                y = void 0,
                                d = Math.floor(p / ut),
                                h = p % ut,
                                pt(y = new Uint8Array(8), d, 0),
                                pt(y, h, 4),
                                y)),
                                e.t2 = Uint8Array,
                                e.next = 18,
                                tt.subtle.sign("HMAC", s, l);
                            case 18:
                                return e.t3 = e.sent.slice(0, a >> 3),
                                f = new e.t2(e.t3),
                                e.abrupt("return", {
                                    ciphertext: u,
                                    tag: f
                                });
                            case 21:
                            case "end":
                                return e.stop()
                            }
                        var p, d, h, y
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            function an(e, t, r, n, o) {
                return cn.apply(this, arguments)
            }
            function cn() {
                return (cn = rn(regeneratorRuntime.mark((function e(t, r, n, o, i) {
                    var a, c, s, u;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (!(n instanceof Uint8Array)) {
                                    e.next = 6;
                                    break
                                }
                                return e.next = 3,
                                tt.subtle.importKey("raw", n, "AES-GCM", !1, ["encrypt"]);
                            case 3:
                                a = e.sent,
                                e.next = 8;
                                break;
                            case 6:
                                $t(n, t, "encrypt"),
                                a = n;
                            case 8:
                                return e.t0 = Uint8Array,
                                e.next = 11,
                                tt.subtle.encrypt({
                                    additionalData: i,
                                    iv: o,
                                    name: "AES-GCM",
                                    tagLength: 128
                                }, a, r);
                            case 11:
                                return e.t1 = e.sent,
                                c = new e.t0(e.t1),
                                s = c.slice(-16),
                                u = c.slice(0, -16),
                                e.abrupt("return", {
                                    ciphertext: u,
                                    tag: s
                                });
                            case 16:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            var sn = function() {
                var e = rn(regeneratorRuntime.mark((function e(t, r, n, o, i) {
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (rt(n) || n instanceof Uint8Array) {
                                    e.next = 2;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [n].concat(Zr(Lt), ["Uint8Array"])));
                            case 2:
                                Mt(t, o),
                                e.t0 = t,
                                e.next = "A128CBC-HS256" === e.t0 || "A192CBC-HS384" === e.t0 || "A256CBC-HS512" === e.t0 ? 6 : "A128GCM" === e.t0 || "A192GCM" === e.t0 || "A256GCM" === e.t0 ? 8 : 10;
                                break;
                            case 6:
                                return n instanceof Uint8Array && Ht(n, parseInt(t.slice(-3), 10)),
                                e.abrupt("return", nn(t, r, n, o, i));
                            case 8:
                                return n instanceof Uint8Array && Ht(n, parseInt(t.slice(1, 4), 10)),
                                e.abrupt("return", an(t, r, n, o, i));
                            case 10:
                                throw new It("Unsupported JWE Content Encryption Algorithm");
                            case 11:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, r, n, o, i) {
                    return e.apply(this, arguments)
                }
            }();
            const un = sn;
            function ln(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function fn(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            ln(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            ln(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function pn(e, t, r, n) {
                return dn.apply(this, arguments)
            }
            function dn() {
                return (dn = fn(regeneratorRuntime.mark((function e(t, r, n, o) {
                    var i, a, c, s;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return i = t.slice(0, 7),
                                o || (o = Ft(i)),
                                e.next = 4,
                                un(i, n, r, o, new Uint8Array(0));
                            case 4:
                                return a = e.sent,
                                c = a.ciphertext,
                                s = a.tag,
                                e.abrupt("return", {
                                    encryptedKey: c,
                                    iv: bt(o),
                                    tag: bt(s)
                                });
                            case 8:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            function hn(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return vn(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || yn(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function yn(e, t) {
                if (e) {
                    if ("string" == typeof e)
                        return vn(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    return "Object" === r && e.constructor && (r = e.constructor.name),
                    "Map" === r || "Set" === r ? Array.from(e) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? vn(e, t) : void 0
                }
            }
            function vn(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            const bn = function(e, t, r, n, o) {
                if (void 0 !== o.crit && void 0 === n.crit)
                    throw new e('"crit" (Critical) Header Parameter MUST be integrity protected');
                if (!n || void 0 === n.crit)
                    return new Set;
                if (!Array.isArray(n.crit) || 0 === n.crit.length || n.crit.some((function(e) {
                    return "string" != typeof e || 0 === e.length
                }
                )))
                    throw new e('"crit" (Critical) Header Parameter MUST be an array of non-empty strings when present');
                var i;
                i = void 0 !== r ? new Map([].concat(hn(Object.entries(r)), hn(t.entries()))) : t;
                var a, c = function(e, t) {
                    var r = "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
                    if (!r) {
                        if (Array.isArray(e) || (r = yn(e)) || t && e && "number" == typeof e.length) {
                            r && (e = r);
                            var n = 0
                              , o = function() {};
                            return {
                                s: o,
                                n: function() {
                                    return n >= e.length ? {
                                        done: !0
                                    } : {
                                        done: !1,
                                        value: e[n++]
                                    }
                                },
                                e: function(e) {
                                    throw e
                                },
                                f: o
                            }
                        }
                        throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                    }
                    var i, a = !0, c = !1;
                    return {
                        s: function() {
                            r = r.call(e)
                        },
                        n: function() {
                            var e = r.next();
                            return a = e.done,
                            e
                        },
                        e: function(e) {
                            c = !0,
                            i = e
                        },
                        f: function() {
                            try {
                                a || null == r.return || r.return()
                            } finally {
                                if (c)
                                    throw i
                            }
                        }
                    }
                }(n.crit);
                try {
                    for (c.s(); !(a = c.n()).done; ) {
                        var s = a.value;
                        if (!i.has(s))
                            throw new It('Extension Header Parameter "'.concat(s, '" is not recognized'));
                        if (void 0 === o[s])
                            throw new e('Extension Header Parameter "'.concat(s, '" is missing'));
                        if (i.get(s) && void 0 === n[s])
                            throw new e('Extension Header Parameter "'.concat(s, '" MUST be integrity protected'))
                    }
                } catch (e) {
                    c.e(e)
                } finally {
                    c.f()
                }
                return new Set(n.crit)
            };
            var gn = ["ext", "key_ops", "alg", "use"];
            function mn(e, t) {
                if (null == e)
                    return {};
                var r, n, o = function(e, t) {
                    if (null == e)
                        return {};
                    var r, n, o = {}, i = Object.keys(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || (o[r] = e[r]);
                    return o
                }(e, t);
                if (Object.getOwnPropertySymbols) {
                    var i = Object.getOwnPropertySymbols(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || Object.prototype.propertyIsEnumerable.call(e, r) && (o[r] = e[r])
                }
                return o
            }
            function wn(e) {
                return function(e) {
                    if (Array.isArray(e))
                        return _n(e)
                }(e) || function(e) {
                    if ("undefined" != typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"])
                        return Array.from(e)
                }(e) || function(e, t) {
                    if (!e)
                        return;
                    if ("string" == typeof e)
                        return _n(e, t);
                    var r = Object.prototype.toString.call(e).slice(8, -1);
                    "Object" === r && e.constructor && (r = e.constructor.name);
                    if ("Map" === r || "Set" === r)
                        return Array.from(e);
                    if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                        return _n(e, t)
                }(e) || function() {
                    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }()
            }
            function _n(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            function On(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            var Sn = function() {
                var e, t = (e = regeneratorRuntime.mark((function e(t) {
                    var r, n;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (!(t instanceof Uint8Array)) {
                                    e.next = 2;
                                    break
                                }
                                return e.abrupt("return", {
                                    kty: "oct",
                                    k: bt(t)
                                });
                            case 2:
                                if (rt(t)) {
                                    e.next = 4;
                                    break
                                }
                                throw new TypeError(Qt.apply(void 0, [t].concat(wn(Lt), ["Uint8Array"])));
                            case 4:
                                if (t.extractable) {
                                    e.next = 6;
                                    break
                                }
                                throw new TypeError("non-extractable CryptoKey cannot be exported as a JWK");
                            case 6:
                                return e.next = 8,
                                tt.subtle.exportKey("jwk", t);
                            case 8:
                                return (r = e.sent).ext,
                                r.key_ops,
                                r.alg,
                                r.use,
                                n = mn(r, gn),
                                e.abrupt("return", n);
                            case 15:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            On(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            On(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                );
                return function(e) {
                    return t.apply(this, arguments)
                }
            }();
            const Pn = Sn;
            function En(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function kn(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            En(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            En(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            function An(e) {
                return xn.apply(this, arguments)
            }
            function xn() {
                return (xn = kn(regeneratorRuntime.mark((function e(t) {
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return e.abrupt("return", Pn(t));
                            case 1:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            var jn = ["encryptedKey"]
              , Cn = ["encryptedKey"];
            function Rn(e, t) {
                if (null == e)
                    return {};
                var r, n, o = function(e, t) {
                    if (null == e)
                        return {};
                    var r, n, o = {}, i = Object.keys(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || (o[r] = e[r]);
                    return o
                }(e, t);
                if (Object.getOwnPropertySymbols) {
                    var i = Object.getOwnPropertySymbols(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || Object.prototype.propertyIsEnumerable.call(e, r) && (o[r] = e[r])
                }
                return o
            }
            function In(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Tn() {
                var e;
                return e = regeneratorRuntime.mark((function e(t, r, n, o) {
                    var i, a, c, s, u, l, f, p, d, h, y, v, b, g, m, w, _, O, S, P = arguments;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                i = P.length > 4 && void 0 !== P[4] ? P[4] : {},
                                Qr(t, n, "encrypt"),
                                e.t0 = t,
                                e.next = "dir" === e.t0 ? 5 : "ECDH-ES" === e.t0 || "ECDH-ES+A128KW" === e.t0 || "ECDH-ES+A192KW" === e.t0 || "ECDH-ES+A256KW" === e.t0 ? 7 : "RSA1_5" === e.t0 || "RSA-OAEP" === e.t0 || "RSA-OAEP-256" === e.t0 || "RSA-OAEP-384" === e.t0 || "RSA-OAEP-512" === e.t0 ? 39 : "PBES2-HS256+A128KW" === e.t0 || "PBES2-HS384+A192KW" === e.t0 || "PBES2-HS512+A256KW" === e.t0 ? 44 : "A128KW" === e.t0 || "A192KW" === e.t0 || "A256KW" === e.t0 ? 53 : "A128GCMKW" === e.t0 || "A192GCMKW" === e.t0 || "A256GCMKW" === e.t0 ? 58 : 67;
                                break;
                            case 5:
                                return s = n,
                                e.abrupt("break", 68);
                            case 7:
                                if (yr(n)) {
                                    e.next = 9;
                                    break
                                }
                                throw new It("ECDH with the provided key is not allowed or not supported by your javascript runtime");
                            case 9:
                                if (u = i.apu,
                                l = i.apv,
                                f = i.epk,
                                e.t1 = f,
                                e.t1) {
                                    e.next = 16;
                                    break
                                }
                                return e.next = 15,
                                dr(n);
                            case 15:
                                f = e.sent.privateKey;
                            case 16:
                                return e.next = 18,
                                An(f);
                            case 18:
                                return p = e.sent,
                                d = p.x,
                                h = p.y,
                                y = p.crv,
                                v = p.kty,
                                e.next = 25,
                                fr(n, f, "ECDH-ES" === t ? r : t, "ECDH-ES" === t ? Ir(r) : parseInt(t.slice(-5, -2), 10), u, l);
                            case 25:
                                if (b = e.sent,
                                c = {
                                    epk: {
                                        x: d,
                                        crv: y,
                                        kty: v
                                    }
                                },
                                "EC" === v && (c.epk.y = h),
                                u && (c.apu = bt(u)),
                                l && (c.apv = bt(l)),
                                "ECDH-ES" !== t) {
                                    e.next = 33;
                                    break
                                }
                                return s = b,
                                e.abrupt("break", 68);
                            case 33:
                                return s = o || Tr(r),
                                g = t.slice(-6),
                                e.next = 37,
                                ar(g, b, s);
                            case 37:
                                return a = e.sent,
                                e.abrupt("break", 68);
                            case 39:
                                return s = o || Tr(r),
                                e.next = 42,
                                Rr(t, n, s);
                            case 42:
                                return a = e.sent,
                                e.abrupt("break", 68);
                            case 44:
                                return s = o || Tr(r),
                                m = i.p2c,
                                w = i.p2s,
                                e.next = 48,
                                Pr(t, n, s, m, w);
                            case 48:
                                return _ = e.sent,
                                a = _.encryptedKey,
                                c = Rn(_, jn),
                                e.abrupt("break", 68);
                            case 53:
                                return s = o || Tr(r),
                                e.next = 56,
                                ar(t, n, s);
                            case 56:
                                return a = e.sent,
                                e.abrupt("break", 68);
                            case 58:
                                return s = o || Tr(r),
                                O = i.iv,
                                e.next = 62,
                                pn(t, n, s, O);
                            case 62:
                                return S = e.sent,
                                a = S.encryptedKey,
                                c = Rn(S, Cn),
                                e.abrupt("break", 68);
                            case 67:
                                throw new It('Invalid or unsupported "alg" (JWE Algorithm) header value');
                            case 68:
                                return e.abrupt("return", {
                                    cek: s,
                                    encryptedKey: a,
                                    parameters: c
                                });
                            case 69:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                Tn = function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            In(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            In(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                ,
                Tn.apply(this, arguments)
            }
            const Dn = function(e, t, r, n) {
                return Tn.apply(this, arguments)
            };
            function Kn(e, t) {
                var r = "undefined" != typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
                if (!r) {
                    if (Array.isArray(e) || (r = function(e, t) {
                        if (!e)
                            return;
                        if ("string" == typeof e)
                            return Fn(e, t);
                        var r = Object.prototype.toString.call(e).slice(8, -1);
                        "Object" === r && e.constructor && (r = e.constructor.name);
                        if ("Map" === r || "Set" === r)
                            return Array.from(e);
                        if ("Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))
                            return Fn(e, t)
                    }(e)) || t && e && "number" == typeof e.length) {
                        r && (e = r);
                        var n = 0
                          , o = function() {};
                        return {
                            s: o,
                            n: function() {
                                return n >= e.length ? {
                                    done: !0
                                } : {
                                    done: !1,
                                    value: e[n++]
                                }
                            },
                            e: function(e) {
                                throw e
                            },
                            f: o
                        }
                    }
                    throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                }
                var i, a = !0, c = !1;
                return {
                    s: function() {
                        r = r.call(e)
                    },
                    n: function() {
                        var e = r.next();
                        return a = e.done,
                        e
                    },
                    e: function(e) {
                        c = !0,
                        i = e
                    },
                    f: function() {
                        try {
                            a || null == r.return || r.return()
                        } finally {
                            if (c)
                                throw i
                        }
                    }
                }
            }
            function Fn(e, t) {
                (null == t || t > e.length) && (t = e.length);
                for (var r = 0, n = new Array(t); r < t; r++)
                    n[r] = e[r];
                return n
            }
            const Mn = function() {
                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                    t[r] = arguments[r];
                var n, o = t.filter(Boolean);
                if (0 === o.length || 1 === o.length)
                    return !0;
                var i, a = Kn(o);
                try {
                    for (a.s(); !(i = a.n()).done; ) {
                        var c = i.value
                          , s = Object.keys(c);
                        if (n && 0 !== n.size)
                            for (var u = 0, l = s; u < l.length; u++) {
                                var f = l[u];
                                if (n.has(f))
                                    return !1;
                                n.add(f)
                            }
                        else
                            n = new Set(s)
                    }
                } catch (e) {
                    a.e(e)
                } finally {
                    a.f()
                }
                return !0
            };
            function Hn(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Un(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Hn(Object(r), !0).forEach((function(t) {
                        Ln(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Hn(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function Ln(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Nn(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Wn(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            var Vn = Symbol()
              , Bn = function() {
                function e(t) {
                    if (function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, e),
                    !(t instanceof Uint8Array))
                        throw new TypeError("plaintext must be an instance of Uint8Array");
                    this._plaintext = t
                }
                var t, r, n, o, i;
                return t = e,
                r = [{
                    key: "setKeyManagementParameters",
                    value: function(e) {
                        if (this._keyManagementParameters)
                            throw new TypeError("setKeyManagementParameters can only be called once");
                        return this._keyManagementParameters = e,
                        this
                    }
                }, {
                    key: "setProtectedHeader",
                    value: function(e) {
                        if (this._protectedHeader)
                            throw new TypeError("setProtectedHeader can only be called once");
                        return this._protectedHeader = e,
                        this
                    }
                }, {
                    key: "setSharedUnprotectedHeader",
                    value: function(e) {
                        if (this._sharedUnprotectedHeader)
                            throw new TypeError("setSharedUnprotectedHeader can only be called once");
                        return this._sharedUnprotectedHeader = e,
                        this
                    }
                }, {
                    key: "setUnprotectedHeader",
                    value: function(e) {
                        if (this._unprotectedHeader)
                            throw new TypeError("setUnprotectedHeader can only be called once");
                        return this._unprotectedHeader = e,
                        this
                    }
                }, {
                    key: "setAdditionalAuthenticatedData",
                    value: function(e) {
                        return this._aad = e,
                        this
                    }
                }, {
                    key: "setContentEncryptionKey",
                    value: function(e) {
                        if (this._cek)
                            throw new TypeError("setContentEncryptionKey can only be called once");
                        return this._cek = e,
                        this
                    }
                }, {
                    key: "setInitializationVector",
                    value: function(e) {
                        if (this._iv)
                            throw new TypeError("setInitializationVector can only be called once");
                        return this._iv = e,
                        this
                    }
                }, {
                    key: "encrypt",
                    value: (o = regeneratorRuntime.mark((function e(t, r) {
                        var n, o, i, a, c, s, u, l, f, p, d, h, y, v, b, g;
                        return regeneratorRuntime.wrap((function(e) {
                            for (; ; )
                                switch (e.prev = e.next) {
                                case 0:
                                    if (this._protectedHeader || this._unprotectedHeader || this._sharedUnprotectedHeader) {
                                        e.next = 2;
                                        break
                                    }
                                    throw new Tt("either setProtectedHeader, setUnprotectedHeader, or sharedUnprotectedHeader must be called before #encrypt()");
                                case 2:
                                    if (Mn(this._protectedHeader, this._unprotectedHeader, this._sharedUnprotectedHeader)) {
                                        e.next = 4;
                                        break
                                    }
                                    throw new Tt("JWE Protected, JWE Shared Unprotected and JWE Per-Recipient Header Parameter names must be disjoint");
                                case 4:
                                    if (n = Un(Un(Un({}, this._protectedHeader), this._unprotectedHeader), this._sharedUnprotectedHeader),
                                    bn(Tt, new Map, null == r ? void 0 : r.crit, this._protectedHeader, n),
                                    void 0 === n.zip) {
                                        e.next = 11;
                                        break
                                    }
                                    if (this._protectedHeader && this._protectedHeader.zip) {
                                        e.next = 9;
                                        break
                                    }
                                    throw new Tt('JWE "zip" (Compression Algorithm) Header MUST be integrity protected');
                                case 9:
                                    if ("DEF" === n.zip) {
                                        e.next = 11;
                                        break
                                    }
                                    throw new It('Unsupported JWE "zip" (Compression Algorithm) Header Parameter value');
                                case 11:
                                    if (o = n.alg,
                                    i = n.enc,
                                    "string" == typeof o && o) {
                                        e.next = 14;
                                        break
                                    }
                                    throw new Tt('JWE "alg" (Algorithm) Header Parameter missing or invalid');
                                case 14:
                                    if ("string" == typeof i && i) {
                                        e.next = 16;
                                        break
                                    }
                                    throw new Tt('JWE "enc" (Encryption Algorithm) Header Parameter missing or invalid');
                                case 16:
                                    if ("dir" !== o) {
                                        e.next = 21;
                                        break
                                    }
                                    if (!this._cek) {
                                        e.next = 19;
                                        break
                                    }
                                    throw new TypeError("setContentEncryptionKey cannot be called when using Direct Encryption");
                                case 19:
                                    e.next = 24;
                                    break;
                                case 21:
                                    if ("ECDH-ES" !== o) {
                                        e.next = 24;
                                        break
                                    }
                                    if (!this._cek) {
                                        e.next = 24;
                                        break
                                    }
                                    throw new TypeError("setContentEncryptionKey cannot be called when using Direct Key Agreement");
                                case 24:
                                    return e.next = 26,
                                    Dn(o, i, t, this._cek, this._keyManagementParameters);
                                case 26:
                                    if (u = e.sent,
                                    c = u.cek,
                                    a = u.encryptedKey,
                                    (s = u.parameters) && (r && Vn in r ? this._unprotectedHeader ? this._unprotectedHeader = Un(Un({}, this._unprotectedHeader), s) : this.setUnprotectedHeader(s) : this._protectedHeader ? this._protectedHeader = Un(Un({}, this._protectedHeader), s) : this.setProtectedHeader(s)),
                                    this._iv || (this._iv = Ft(i)),
                                    f = this._protectedHeader ? ct.encode(bt(JSON.stringify(this._protectedHeader))) : ct.encode(""),
                                    this._aad ? (p = bt(this._aad),
                                    l = lt(f, ct.encode("."), ct.encode(p))) : l = f,
                                    "DEF" !== n.zip) {
                                        e.next = 45;
                                        break
                                    }
                                    return e.next = 37,
                                    ((null == r ? void 0 : r.deflateRaw) || Vt)(this._plaintext);
                                case 37:
                                    return y = e.sent,
                                    e.next = 40,
                                    un(i, y, c, this._iv, l);
                                case 40:
                                    v = e.sent,
                                    d = v.ciphertext,
                                    h = v.tag,
                                    e.next = 51;
                                    break;
                                case 45:
                                    return e.next = 48,
                                    un(i, this._plaintext, c, this._iv, l);
                                case 48:
                                    b = e.sent,
                                    d = b.ciphertext,
                                    h = b.tag;
                                case 51:
                                    return g = {
                                        ciphertext: bt(d),
                                        iv: bt(this._iv),
                                        tag: bt(h)
                                    },
                                    a && (g.encrypted_key = bt(a)),
                                    p && (g.aad = p),
                                    this._protectedHeader && (g.protected = st.decode(f)),
                                    this._sharedUnprotectedHeader && (g.unprotected = this._sharedUnprotectedHeader),
                                    this._unprotectedHeader && (g.header = this._unprotectedHeader),
                                    e.abrupt("return", g);
                                case 58:
                                case "end":
                                    return e.stop()
                                }
                        }
                        ), e, this)
                    }
                    )),
                    i = function() {
                        var e = this
                          , t = arguments;
                        return new Promise((function(r, n) {
                            var i = o.apply(e, t);
                            function a(e) {
                                Nn(i, r, n, a, c, "next", e)
                            }
                            function c(e) {
                                Nn(i, r, n, a, c, "throw", e)
                            }
                            a(void 0)
                        }
                        ))
                    }
                    ,
                    function(e, t) {
                        return i.apply(this, arguments)
                    }
                    )
                }],
                r && Wn(t.prototype, r),
                n && Wn(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                e
            }();
            function Gn(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Jn(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            var zn = function() {
                function e(t) {
                    !function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, e),
                    this._flattened = new Bn(t)
                }
                var t, r, n, o, i;
                return t = e,
                r = [{
                    key: "setContentEncryptionKey",
                    value: function(e) {
                        return this._flattened.setContentEncryptionKey(e),
                        this
                    }
                }, {
                    key: "setInitializationVector",
                    value: function(e) {
                        return this._flattened.setInitializationVector(e),
                        this
                    }
                }, {
                    key: "setProtectedHeader",
                    value: function(e) {
                        return this._flattened.setProtectedHeader(e),
                        this
                    }
                }, {
                    key: "setKeyManagementParameters",
                    value: function(e) {
                        return this._flattened.setKeyManagementParameters(e),
                        this
                    }
                }, {
                    key: "encrypt",
                    value: (o = regeneratorRuntime.mark((function e(t, r) {
                        var n;
                        return regeneratorRuntime.wrap((function(e) {
                            for (; ; )
                                switch (e.prev = e.next) {
                                case 0:
                                    return e.next = 2,
                                    this._flattened.encrypt(t, r);
                                case 2:
                                    return n = e.sent,
                                    e.abrupt("return", [n.protected, n.encrypted_key, n.iv, n.ciphertext, n.tag].join("."));
                                case 4:
                                case "end":
                                    return e.stop()
                                }
                        }
                        ), e, this)
                    }
                    )),
                    i = function() {
                        var e = this
                          , t = arguments;
                        return new Promise((function(r, n) {
                            var i = o.apply(e, t);
                            function a(e) {
                                Gn(i, r, n, a, c, "next", e)
                            }
                            function c(e) {
                                Gn(i, r, n, a, c, "throw", e)
                            }
                            a(void 0)
                        }
                        ))
                    }
                    ,
                    function(e, t) {
                        return i.apply(this, arguments)
                    }
                    )
                }],
                r && Jn(t.prototype, r),
                n && Jn(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                e
            }();
            function Yn(e) {
                var t, r;
                function n(t, r) {
                    try {
                        var i = e[t](r)
                          , a = i.value
                          , c = a instanceof $n;
                        Promise.resolve(c ? a.v : a).then((function(r) {
                            if (c) {
                                var s = "return" === t ? "return" : "next";
                                if (!a.k || r.done)
                                    return n(s, r);
                                r = e[s](r).value
                            }
                            o(i.done ? "return" : "normal", r)
                        }
                        ), (function(e) {
                            n("throw", e)
                        }
                        ))
                    } catch (e) {
                        o("throw", e)
                    }
                }
                function o(e, o) {
                    switch (e) {
                    case "return":
                        t.resolve({
                            value: o,
                            done: !0
                        });
                        break;
                    case "throw":
                        t.reject(o);
                        break;
                    default:
                        t.resolve({
                            value: o,
                            done: !1
                        })
                    }
                    (t = t.next) ? n(t.key, t.arg) : r = null
                }
                this._invoke = function(e, o) {
                    return new Promise((function(i, a) {
                        var c = {
                            key: e,
                            arg: o,
                            resolve: i,
                            reject: a,
                            next: null
                        };
                        r ? r = r.next = c : (t = r = c,
                        n(e, o))
                    }
                    ))
                }
                ,
                "function" != typeof e.return && (this.return = void 0)
            }
            function $n(e, t) {
                this.v = e,
                this.k = t
            }
            Yn.prototype["function" == typeof Symbol && Symbol.asyncIterator || "@@asyncIterator"] = function() {
                return this
            }
            ,
            Yn.prototype.next = function(e) {
                return this._invoke("next", e)
            }
            ,
            Yn.prototype.throw = function(e) {
                return this._invoke("throw", e)
            }
            ,
            Yn.prototype.return = function(e) {
                return this._invoke("return", e)
            }
            ;
            var qn = bt;
            function Xn(e) {
                if (!e)
                    return new Uint8Array(0);
                e.length % 2 == 1 && (e = "0" + e);
                for (var t = e.length / 2, r = new Uint8Array(t), n = 0; n < t; n++)
                    r[n] = parseInt(e.substr(2 * n, 2), 16);
                return r
            }
            function Qn(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Zn(e) {
                return eo.apply(this, arguments)
            }
            function eo() {
                var e;
                return e = regeneratorRuntime.mark((function e(t) {
                    var r, n, o, i, a, c, s, u, l;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (2 === (r = t.split("|")).length) {
                                    e.next = 3;
                                    break
                                }
                                throw new Error("Malformed public key: type 1");
                            case 3:
                                return n = r[0],
                                o = r[1],
                                i = Xn(n),
                                a = Xn(o),
                                c = qn(i),
                                s = qn(a),
                                u = {
                                    kty: "RSA",
                                    kid: "asf-key",
                                    e: c,
                                    n: s
                                },
                                e.next = 12,
                                Yr(u, _e);
                            case 12:
                                if (l = e.sent,
                                window.skipKeyLengthCheckForUnitTests || 2048 === l.algorithm.modulusLength) {
                                    e.next = 15;
                                    break
                                }
                                throw new Error("Malformed public key: type 2");
                            case 15:
                                return e.abrupt("return", l);
                            case 16:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                eo = function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            Qn(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            Qn(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                ,
                eo.apply(this, arguments)
            }
            function to(e) {
                var t, r = this, n = e.txVariant;
                this.txVariant = n,
                this.props.fieldType = e.fieldType,
                window.sfConfigLog.d_handlingConfig = !0,
                window.sfConfigLog.e_fieldType = this.props.fieldType,
                this.props.extraFieldData = null;
                try {
                    this.props.extraFieldData = JSON.parse(e.extraFieldData)
                } catch (e) {}
                if (this.props.numKey = e.numKey,
                this.props.legacyInputMode = e.legacyInputMode,
                this.props.uniqueIdFromLabel = e.uid,
                e.isCreditCardType && (t = H(n, e.cardGroupTypes),
                this.props.trimTrailingSeparator = !(!1 === e.trimTrailingSeparator),
                this.props.isSingleBrandedCard = t.isSingleBrandedCard,
                this.props.cardBrand = t.cardBrand,
                this.props.cardGroupTypes = t.cardGroupTypes,
                this.props.cvcPolicy = e.cvcPolicy,
                this.props.maskSecurityCode = e.maskSecurityCode,
                this.props.expiryDatePolicy = e.expiryDatePolicy,
                this.props.minimumExpiryDate = e.minimumExpiryDate,
                this.props.exposeExpiryDate = e.exposeExpiryDate,
                this.props.disableIOSArrowKeys = e.disableIOSArrowKeys),
                this.showWarnings = e.showWarnings,
                this.props.implementationType = e.implementationType,
                "undefined" == typeof adyen)
                    return this.showWarnings && M("WARNING: securedFields:: the expected top level object is not present. Error: type 7"),
                    window.sfConfigLog.z_errors.push("CONFIG_MSG_REJECTED_TYPE_7"),
                    ne;
                if (!adyen.key || !adyen.key.length)
                    return this.showWarnings && M("WARNING: securedFields:: the encryption key is not present. It will not be possible to encrypt input fields. Error: type 8"),
                    window.sfConfigLog.z_errors.push("CONFIG_MSG_REJECTED_TYPE_8"),
                    oe;
                window.sfConfigLog.f_processedStylesStart = (new Date).getTime(),
                We.process(e.iframeUIConfig.sfStyles),
                window.sfConfigLog.g_processedStylesStop = (new Date).getTime(),
                this.props.placeholdersConfig = e.iframeUIConfig.placeholders,
                this.props.ariaConfig = e.iframeUIConfig.ariaConfig,
                qe(this.props.ariaConfig, "lang") && document.getElementsByTagName("html")[0].setAttribute("lang", this.props.ariaConfig.lang.toString());
                var o = qe(this.props.ariaConfig, "".concat(this.props.fieldType, ".iframeTitle"));
                return o && document.getElementsByTagName("head")[0].setAttribute("title", o),
                window.sfConfigLog.h_beginningKeyGen = !0,
                Zn(adyen.key).then((function(t) {
                    r.props.encryptionKey = t,
                    window.sfHasConfigured = !0,
                    window.sfConfigLog.i_configured = !0;
                    var n = U(document, "#originErrorField");
                    n && U(document, "body").removeChild(n);
                    r.setState({
                        status: e.fieldType
                    })
                }
                )).catch((function(e) {
                    window.sfConfigLog.z_errors.push(e.toString())
                }
                )),
                re
            }
            const ro = function(e, t) {
                return Number(e) === t || (M("WARNING: securedFields:: postMessage special data is incorrect: type 5"),
                !1)
            };
            function no(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function oo(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function io(e) {
                if (!(Object.prototype.hasOwnProperty.call(e, "txVariant") && Object.prototype.hasOwnProperty.call(e, "fieldType") && Object.prototype.hasOwnProperty.call(e, "numKey")))
                    return this.showWarnings && M("\nWARNING: securedFields:: postMessage special data is incorrect: type 4"),
                    ae;
                if (!ro(e.numKey, this.props.numKey))
                    return ce;
                var t, r, n = function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = null != arguments[t] ? arguments[t] : {};
                        t % 2 ? no(Object(r), !0).forEach((function(t) {
                            oo(e, t, r[t])
                        }
                        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : no(Object(r)).forEach((function(t) {
                            Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                        }
                        ))
                    }
                    return e
                }({}, e);
                if (n.focus)
                    return this.sfCompRef.specialMessageOnFocus(),
                    ie;
                if (n.styleObject)
                    return We.update(n.styleObject),
                    ie;
                if (Object.prototype.hasOwnProperty.call(n, "destroy"))
                    return K(null, document.body, this.base),
                    ie;
                if (n.fieldClick)
                    return this.sfCompRef.specialMessageOnClick(n),
                    ie;
                if (n.checkoutTouchEvent)
                    return null === (t = (r = this.sfCompRef).specialMessageOnCheckoutTouchEvent) || void 0 === t || t.call(r, n),
                    ie;
                if (n.brand)
                    return ("card" === this.txVariant || "bcmc" === this.txVariant && this.props.fieldType === J) && this.sfCompRef.specialMessageOnBrand(n),
                    ie;
                if (Object.prototype.hasOwnProperty.call(n, "unsupportedCard")) {
                    if (!0 === n.unsupportedCard && n.code.length)
                        return this.sfCompRef.specialMessageUnsupportedCard(n),
                        ie;
                    if (!1 === n.unsupportedCard && 0 === n.code.length)
                        return this.sfCompRef.specialMessageUnsupportedCard(null),
                        ie
                }
                return n.externalValidation ? (this.sfCompRef.specialMessageExternalValidation(n),
                ie) : n.autoComplete ? (this.sfCompRef.specialMessageAutoComplete(n),
                ie) : n.code ? (this.sfCompRef.specialMessageOnCode(n),
                ie) : n.expiryDatePolicy ? (this.sfCompRef.specialMessageExpiryDatePolicy(n),
                ie) : ie
            }
            function ao(e) {
                var t, r = e.origin || e.originalEvent.origin, n = origin.length - 1;
                if ("/" === origin.charAt(n) && (origin = origin.substring(0, n)),
                r !== origin)
                    return Z;
                if ("string" != typeof e.data)
                    return this.showWarnings && M("\nWARNING: securedFields:: postMessage data is incorrect: type 1"),
                    ee;
                try {
                    t = JSON.parse(e.data)
                } catch (e) {
                    return this.showWarnings && M("\nWARNING: securedFields:: postMessage data is incorrect: type 2"),
                    te
                }
                return function(e) {
                    return Object.prototype.hasOwnProperty.call(e, "txVariant") && Object.prototype.hasOwnProperty.call(e, "fieldType") && Object.prototype.hasOwnProperty.call(e, "extraFieldData") && Object.prototype.hasOwnProperty.call(e, "numKey") && Object.prototype.hasOwnProperty.call(e, "cardGroupTypes") && Object.prototype.hasOwnProperty.call(e, "isCreditCardType") && Object.prototype.hasOwnProperty.call(e, "showWarnings") && Object.prototype.hasOwnProperty.call(e, "sfLogAtStart")
                }(t) ? (this.eventOrigin = r,
                this.eventSource = e.source,
                this.handleConfigMessage(t)) : function(e) {
                    return !!(Object.prototype.hasOwnProperty.call(e, "focus") || Object.prototype.hasOwnProperty.call(e, "brand") || Object.prototype.hasOwnProperty.call(e, "destroy") || Object.prototype.hasOwnProperty.call(e, "styleObject") || Object.prototype.hasOwnProperty.call(e, "fieldClick") || Object.prototype.hasOwnProperty.call(e, "checkoutTouchEvent") || Object.prototype.hasOwnProperty.call(e, "_b$dl") || Object.prototype.hasOwnProperty.call(e, "externalValidation") || Object.prototype.hasOwnProperty.call(e, "unsupportedCard") || Object.prototype.hasOwnProperty.call(e, "code") || Object.prototype.hasOwnProperty.call(e, "autoComplete") || Object.prototype.hasOwnProperty.call(e, "expiryDatePolicy"))
                }(t) ? this.handleSpecialMessage(t) : (M("\nWARNING: securedFields:: postMessage data is incorrect: type 6"),
                se)
            }
            function co(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function so(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function uo(e) {
                if (!Object.prototype.hasOwnProperty.call(e, "action") || Object.prototype.hasOwnProperty.call(e, "action") && "" === e.action)
                    throw new Error("message not sent: no action set");
                var t = function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = null != arguments[t] ? arguments[t] : {};
                        t % 2 ? co(Object(r), !0).forEach((function(t) {
                            so(e, t, r[t])
                        }
                        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : co(Object(r)).forEach((function(t) {
                            Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                        }
                        ))
                    }
                    return e
                }({}, e);
                t.fieldType = this.props.fieldType,
                t.numKey = this.props.numKey;
                var r = JSON.stringify(t);
                return this.eventSource.postMessage(r, this.eventOrigin),
                r
            }
            var lo = /(android)/i.test(navigator.userAgent)
              , fo = function() {
                var e = navigator.userAgent
                  , t = e.indexOf("MSIE ");
                if (t > 0)
                    return parseInt(e.substring(t + 5, e.indexOf(".", t)), 10);
                if (e.indexOf("Trident/") > 0) {
                    var r = e.indexOf("rv:");
                    return parseInt(e.substring(r + 3, e.indexOf(".", r)), 10)
                }
                var n = e.indexOf("Edge/");
                if (n > 0)
                    return parseInt(e.substring(n + 5, e.indexOf(".", n)), 10);
                return !1
            }()
              , po = /iphone|ipod|ipad/i.test(navigator.userAgent);
            const ho = {
                __IS_ANDROID: lo,
                __IS_IE: fo,
                __IS_IOS: po,
                __IS_CHROME_IOS: po && /crios/i.test(navigator.userAgent),
                __IS_FIREFOX: /(firefox)/i.test(navigator.userAgent),
                __IS_SAFARI: /(safari)/i.test(navigator.userAgent) && !/(chrome)/i.test(navigator.userAgent)
            };
            var yo, vo, bo, go, mo = function() {
                ho.__IS_SAFARI ? !1 === go.safariTabFixApplied && (go.safariTabFixApplied = !0,
                setTimeout((function() {
                    U(document, "#".concat(yo)).focus()
                }
                ), 200)) : U(document, "#".concat(yo)).focus()
            }, wo = function() {
                bo.call(go, {
                    action: "shifttab"
                })
            }, _o = function() {
                (ho.__IS_FIREFOX || ho.__IS_IE && ho.__IS_IE <= 11) && ((vo = U(document, "#shiftTabField")).setAttribute("tabindex", 0),
                L(vo, "focus", wo))
            }, Oo = function(e, t, r) {
                yo = e,
                bo = t,
                go = r,
                (ho.__IS_FIREFOX || ho.__IS_IE && ho.__IS_IE <= 11 || ho.__IS_SAFARI) && L(window, "focus", mo),
                setTimeout(_o, 0)
            };
            function So(e) {
                return So = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                So(e)
            }
            function Po(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            function Eo(e, t) {
                return Eo = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                    return e.__proto__ = t,
                    e
                }
                ,
                Eo(e, t)
            }
            function ko(e) {
                var t = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}
                        ))),
                        !0
                    } catch (e) {
                        return !1
                    }
                }();
                return function() {
                    var r, n = xo(e);
                    if (t) {
                        var o = xo(this).constructor;
                        r = Reflect.construct(n, arguments, o)
                    } else
                        r = n.apply(this, arguments);
                    return function(e, t) {
                        if (t && ("object" === So(t) || "function" == typeof t))
                            return t;
                        if (void 0 !== t)
                            throw new TypeError("Derived constructors may only return object or undefined");
                        return Ao(e)
                    }(this, r)
                }
            }
            function Ao(e) {
                if (void 0 === e)
                    throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                return e
            }
            function xo(e) {
                return xo = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                    return e.__proto__ || Object.getPrototypeOf(e)
                }
                ,
                xo(e)
            }
            var jo = function(e) {
                !function(e, t) {
                    if ("function" != typeof t && null !== t)
                        throw new TypeError("Super expression must either be null or a function");
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    Object.defineProperty(e, "prototype", {
                        writable: !1
                    }),
                    t && Eo(e, t)
                }(i, e);
                var t, r, n, o = ko(i);
                function i(e) {
                    var t, r, n, a;
                    return function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, i),
                    t = o.call(this, e),
                    r = Ao(t),
                    a = function(e) {
                        t.sfCompRef = e
                    }
                    ,
                    (n = "handleComponentRef")in r ? Object.defineProperty(r, n, {
                        value: a,
                        enumerable: !0,
                        configurable: !0,
                        writable: !0
                    }) : r[n] = a,
                    t.setState({
                        status: "configuring"
                    }),
                    t.messageReceiver = ao.bind(Ao(t)),
                    t.handleConfigMessage = to,
                    t.handleSpecialMessage = io,
                    t.sendPostMessage = uo,
                    t.tabbingFixesAddCount = 0,
                    t.safariTabFixApplied = !1,
                    t.onChange = t.onChange.bind(Ao(t)),
                    t.init(),
                    t
                }
                return t = i,
                r = [{
                    key: "init",
                    value: function() {
                        L(window, "message", this.messageReceiver, !1),
                        window.sfConfigLog.b_type = this.props.type,
                        window.sfConfigLog.c_listenerAdded = !0
                    }
                }, {
                    key: "onChange",
                    value: function(e) {
                        this.sendPostMessage(e)
                    }
                }, {
                    key: "componentDidMount",
                    value: function() {}
                }, {
                    key: "shouldComponentUpdate",
                    value: function() {
                        return "configuring" === this.state.status
                    }
                }, {
                    key: "componentDidUpdate",
                    value: function(e, t) {
                        if ("configuring" === t.status) {
                            if (this.tabbingFixesAddCount += 1,
                            this.tabbingFixesAddCount >= 2)
                                throw new Error("Tabbing Fixes being added more than once");
                            Oo(this.props.uniqueIdFromLabel || this.props.fieldType, this.onChange, this),
                            "object" === So(this.sfCompRef) && (window.sfConfigLog.k_sendingConfigConfirmation = !0,
                            this.onChange({
                                action: "config"
                            }))
                        }
                    }
                }, {
                    key: "componentWillUnmount",
                    value: function() {
                        this.sfCompRef = null,
                        N(window, "message", this.messageReceiver, !1),
                        (ho.__IS_FIREFOX || ho.__IS_IE && ho.__IS_IE <= 11) && (N(window, "focus", mo),
                        N(vo, "focus", wo))
                    }
                }, {
                    key: "render",
                    value: function(e) {
                        var t = e.SFFactory
                          , r = e.type;
                        return "configuring" !== this.state.status ? (r && (window.sfConfigLog.j_renderedField = !0),
                        t(this.props, this.state, this.handleComponentRef, this.onChange)) : null
                    }
                }],
                r && Po(t.prototype, r),
                n && Po(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                i
            }(v);
            const Co = jo;
            const Ro = function(e, t) {
                var r;
                window.origin = window.origin || origin,
                window.originKey = window.originKey || originKey,
                window.genTime = window.genTime || genTime,
                window.checkoutShopperUrl = window.checkoutShopperUrl || checkoutShopperUrl,
                window.sfConfigLog = {
                    a_sfInit: !0,
                    z_errors: [],
                    b_type: void 0,
                    c_listenerAdded: void 0,
                    d_handlingConfig: void 0,
                    e_fieldType: void 0,
                    f_processedStylesStart: void 0,
                    g_processedStylesStop: void 0,
                    h_beginningKeyGen: void 0,
                    i_configured: void 0,
                    j_renderedField: void 0,
                    k_sendingConfigConfirmation: void 0
                };
                var n = document.location.origin || "".concat(document.location.protocol, "//").concat(document.location.host)
                  , o = n + document.location.pathname;
                return window.checkoutShopperUrl.indexOf("-live") > -1 && -1 === window.origin.indexOf("https") ? (window.sfConfigLog.z_errors.push("Merchant origin is insecure (not https)"),
                !1) : (r = "".concat(window.checkoutShopperUrl, "securedfields/").concat(window.originKey, "/").concat("4.9.0", "/securedFields.html")) !== o ? (window.console && window.console.error && window.console.error("ERROR: sfInit:: Invalid hosting of SecuredFields file.  Document origin: ", n, "Permitted src=", r, "Actual src=", o),
                !1) : (K(d(Co, {
                    SFFactory: e,
                    type: t
                }), document.body),
                !0)
            };
            function Io(e) {
                var t = this;
                return new Promise((function(r) {
                    "" !== e.error || t.state.hasUnsupportedCard ? r(t.handleErrorOnField(e)) : t.isValidLength ? r(t.handleValidField(e)) : r(t.handleInvalidField(e))
                }
                ))
            }
            function To(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Do(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Ko(e) {
                var t = function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = null != arguments[t] ? arguments[t] : {};
                        t % 2 ? To(Object(r), !0).forEach((function(t) {
                            Do(e, t, r[t])
                        }
                        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : To(Object(r)).forEach((function(t) {
                            Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                        }
                        ))
                    }
                    return e
                }({}, e)
                  , r = t.error;
                return this.state.hasUnsupportedCard && (r = we),
                t.error = r,
                t = et("endDigits").from(t),
                {
                    onChangeObj: this.state.hasUnsupportedCard ? null : t,
                    stateObj: {
                        status: "errorOnField",
                        showAsValid: !1,
                        ariaInvalid: !0,
                        error: r
                    }
                }
            }
            function Fo(e) {
                var t = null
                  , r = null;
                return this.setState((function(e) {
                    return t = e.showAsValid,
                    r = "" !== e.error,
                    {}
                }
                )),
                t || r ? {
                    onChangeObj: e,
                    stateObj: {
                        showAsValid: !1,
                        ariaInvalid: !1,
                        error: ""
                    }
                } : {
                    onChangeObj: null,
                    stateObj: {}
                }
            }
            function Mo(e) {
                return e.charAt(e.length - 1)
            }
            function Ho(e, t) {
                var r = t || 1;
                return e.substr(0, e.length - r)
            }
            function Uo(e, t) {
                var r = t || "some";
                return 1 === e.length && "number" == typeof parseInt(e) ? r + pe : e || r
            }
            function Lo(e, t) {
                var r = he[+e]
                  , n = ye.indexOf(r);
                if (n > 9) {
                    var o = String(n).split("")
                      , i = t.lastIndexOf(o[0])
                      , a = t.lastIndexOf(o[1]);
                    return "".concat(i, "_").concat(a)
                }
                return String(t.lastIndexOf(n))
            }
            function No(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Wo(e) {
                return function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            No(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            No(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
            }
            var Vo = function() {
                var e = Wo(regeneratorRuntime.mark((function e(t, r) {
                    var n, o, i, a, c = arguments;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return n = c.length > 2 && void 0 !== c[2] ? c[2] : "A256CBC-HS512",
                                o = c.length > 3 && void 0 !== c[3] ? c[3] : _e,
                                i = (new TextEncoder).encode(JSON.stringify(t)),
                                e.next = 5,
                                new zn(i).setProtectedHeader({
                                    alg: o,
                                    enc: n,
                                    version: "1"
                                }).encrypt(r).catch((function(e) {
                                    console.warn("### encryptJWE:: encrypt error:: e=", e)
                                }
                                ));
                            case 5:
                                return a = e.sent,
                                e.abrupt("return", a);
                            case 7:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )));
                return function(t, r) {
                    return e.apply(this, arguments)
                }
            }();
            function Bo(e, t) {
                return Go.apply(this, arguments)
            }
            function Go() {
                return (Go = Wo(regeneratorRuntime.mark((function e(t, r) {
                    var n;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                if (r) {
                                    e.next = 3;
                                    break
                                }
                                return console.warn("WARNING: No encryptionKey"),
                                e.abrupt("return", null);
                            case 3:
                                return e.next = 5,
                                Vo(t, r);
                            case 5:
                                return n = e.sent,
                                e.abrupt("return", n);
                            case 7:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )))).apply(this, arguments)
            }
            function Jo(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function zo(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            var Yo = function() {
                var e, t = (e = regeneratorRuntime.mark((function e(t) {
                    var r, n, o, i, a, c, s, u, l, f, p, d, h, y;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return n = t.valToEncrypt,
                                o = t.encryptionType,
                                i = t.encryptionKey,
                                a = t.encryptionName,
                                c = t.fieldType,
                                s = t.eventLogger,
                                (u = {}).type = o,
                                u.action = "encryption",
                                l = Bo,
                                Jo(r = {}, a, n),
                                Jo(r, "generationtime", window.genTime),
                                f = r,
                                p = s ? s.mergeLog(f) : f,
                                e.next = 9,
                                l(p, i);
                            case 9:
                                return d = e.sent,
                                h = !!d,
                                y = function() {
                                    var e, t = o;
                                    "month" !== o && "year" !== o || (t = "encryptedExpiry".concat((e = o).charAt(0).toUpperCase() + e.slice(1)));
                                    var r = [];
                                    return r.push({
                                        type: o,
                                        encryptedFieldName: t,
                                        blob: d
                                    }),
                                    u[c] = r,
                                    u
                                }
                                ,
                                e.abrupt("return", h ? y() : null);
                            case 13:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e)
                }
                )),
                function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            zo(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            zo(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                );
                return function(e) {
                    return t.apply(this, arguments)
                }
            }();
            function $o(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function qo(e, t, r, n) {
                return Xo.apply(this, arguments)
            }
            function Xo() {
                var e;
                return e = regeneratorRuntime.mark((function e(t, r, n, o) {
                    var i, a, c, s;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return i = this.props.fieldType,
                                a = qe(this, r),
                                c = {
                                    valToEncrypt: a,
                                    encryptionType: i,
                                    encryptionKey: this.props.encryptionKey,
                                    eventLogger: this.eventLogger,
                                    encryptionName: t,
                                    fieldType: i
                                },
                                e.next = 5,
                                Yo(c);
                            case 5:
                                if (!(s = e.sent)) {
                                    e.next = 10;
                                    break
                                }
                                return n.map((function(e) {
                                    return Object.prototype.hasOwnProperty.call(o, e) && (s[e] = o[e]),
                                    !0
                                }
                                )),
                                i === B && (s.code = Lo(a, s[B][0].blob)),
                                e.abrupt("return", {
                                    onChangeObj: s,
                                    stateObj: {
                                        showAsValid: !0,
                                        ariaInvalid: !1,
                                        error: ""
                                    }
                                });
                            case 10:
                                return console.warn("### handleValidField::ENCRYPTION FAIL:: encryptedObj=", s),
                                e.abrupt("return", {
                                    onChangeObj: null,
                                    stateObj: {}
                                });
                            case 12:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, this)
                }
                )),
                Xo = function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            $o(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            $o(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                ,
                Xo.apply(this, arguments)
            }
            function Qo(e) {
                var t = e.substr(0, 2)
                  , r = e.substr(2, 4);
                return t.length ? t + X + r : ""
            }
            function Zo(e) {
                var t = 0
                  , r = e.split(X)
                  , n = [];
                if (r.forEach((function(e) {
                    if ("" !== e) {
                        var t = e.replace(/[^\d]/g, "");
                        n.push(t)
                    }
                }
                )),
                2 === n.length && 1 === n[0].length) {
                    var o = n[1].substr(0, 1);
                    n[0] += o,
                    n[1] = n[1].substr(1),
                    t = 2
                }
                return {
                    dateArr: n,
                    cursorPosFlag: t,
                    originalVal: e
                }
            }
            function ei(e) {
                return {
                    unmaskedVal: e.replace(/[^\d]/g, ""),
                    originalVal: e
                }
            }
            function ti(e, t) {
                var r = Math.floor(e / t);
                return e % t > 0 ? r : r - 1
            }
            const ri = function(e) {
                var t = e;
                return t.fireEvent = function(e, t, r, n) {
                    var o;
                    try {
                        o = new Event(t),
                        r && n && (o[r] = n)
                    } catch (r) {
                        if (!document.createEvent)
                            return void e.fireEvent("on".concat(t));
                        (o = document.createEvent("Event")).initEvent(t, !1, !1)
                    }
                    e.dispatchEvent(o)
                }
                ,
                t
            };
            var ni = "delete"
              , oi = function(e, t) {
                switch (t) {
                case "key":
                case "code":
                    return "Backspace" === e || "Delete" === e ? ni : "ArrowLeft" === e ? "leftarrow" : "ArrowRight" === e ? "rightarrow" : " " === e || "Space" === e ? "space" : "Shift" === e || "ShiftRight" === e || "ShiftLeft" === e ? "shift" : "Tab" === e ? "tab" : "Unidentified" === e ? "androidkeystroke" : e;
                case "keyCode":
                case "which":
                    return 8 === e || 46 === e ? ni : 37 === e ? "leftarrow" : 39 === e ? "rightarrow" : 32 === e ? "space" : 16 === e ? "shift" : 9 === e ? "tab" : 229 === e ? "androidkeystroke" : String.fromCharCode(e);
                default:
                    return e
                }
            };
            const ii = {
                handleKeyPress: function(e) {
                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : oi;
                    return void 0 !== e.key ? t(e.key, "key") : void 0 !== e.code && "" !== e.code ? t(e.code, "code") : e.keyCode >= 0 ? t(e.keyCode, "keyCode") : void 0 !== e.which && t(e.which, "which")
                },
                getCaretPos: function(e, t) {
                    var r = !0 === t ? "selectionEnd" : "selectionStart";
                    return r in e ? e[r] : 0
                },
                setSelectionRange: function(e, t, r) {
                    var n = r || t;
                    e.setSelectionRange && (e.focus(),
                    e.setSelectionRange(t, n))
                },
                __DELETE_OR_BACKSPACE: ni,
                __X_KEY: "xKeyPressed"
            };
            function ai(e) {
                var t = this.fieldRef
                  , r = {};
                if (ri(r),
                this.props.fieldType === e.fieldType) {
                    if (this.props.disableIOSArrowKeys && this.setState({
                        shouldDisableField: !1
                    }),
                    this.hasFocus) {
                        var n = t.value
                          , o = ii.getCaretPos(t);
                        return t.value = n,
                        ii.setSelectionRange(t, o),
                        "handleClickMessage: Field types match, securedField has focus - reset field value & set caret pos"
                    }
                    return r.fireEvent(t, "focus"),
                    "handleClickMessage: Field types match, securedField does not have focus - fire focus event"
                }
                return ho.__IS_IOS && this.props.disableIOSArrowKeys && this.setState({
                    shouldDisableField: !0
                }),
                this.hasFocus ? (r.fireEvent(t, "blur"),
                this.hasFocus = !1,
                t.disabled = !0,
                setTimeout((function() {
                    t.disabled = !1
                }
                ), 10),
                "handleClickMessage: Field types do not match but this securedField does have focus so force it to blur") : "handleClickMessage: Field types do not match but this securedField does not have focus so do nothing"
            }
            function ci(e) {
                if (this.props.fieldType === e.fieldType && !0 === e.externalValidation) {
                    var t = e.code;
                    return t || console.warn("WARNING: handleExternalValidation - no error code has been sent"),
                    this.setState({
                        showAsValid: !1,
                        ariaInvalid: !0,
                        isDirty: !0,
                        error: t
                    }),
                    !0
                }
                return !1
            }
            function si(e) {
                var t = !(arguments.length > 1 && void 0 !== arguments[1]) || arguments[1]
                  , r = {};
                ri(r),
                t && (this.fieldRef.value = e.autoComplete,
                r.fireEvent(this.fieldRef, "paste")),
                r.fireEvent(this.fieldRef, "input")
            }
            function ui() {
                this.state.isDirty || this.setState({
                    isDirty: !0
                })
            }
            function li(e) {
                return li = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                li(e)
            }
            function fi(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            function pi(e, t) {
                return pi = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                    return e.__proto__ = t,
                    e
                }
                ,
                pi(e, t)
            }
            function di(e) {
                var t = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}
                        ))),
                        !0
                    } catch (e) {
                        return !1
                    }
                }();
                return function() {
                    var r, n = hi(e);
                    if (t) {
                        var o = hi(this).constructor;
                        r = Reflect.construct(n, arguments, o)
                    } else
                        r = n.apply(this, arguments);
                    return function(e, t) {
                        if (t && ("object" === li(t) || "function" == typeof t))
                            return t;
                        if (void 0 !== t)
                            throw new TypeError("Derived constructors may only return object or undefined");
                        return function(e) {
                            if (void 0 === e)
                                throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                            return e
                        }(e)
                    }(this, r)
                }
            }
            function hi(e) {
                return hi = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                    return e.__proto__ || Object.getPrototypeOf(e)
                }
                ,
                hi(e)
            }
            var yi, vi, bi, gi = "is-autofilled", mi = function(e) {
                !function(e, t) {
                    if ("function" != typeof t && null !== t)
                        throw new TypeError("Super expression must either be null or a function");
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    Object.defineProperty(e, "prototype", {
                        writable: !1
                    }),
                    t && pi(e, t)
                }(i, e);
                var t, r, n, o = di(i);
                function i(e) {
                    var t;
                    !function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, i);
                    var r = (t = o.call(this, e)).processConfigObjects(t.props);
                    return t.props.ariaErrorText = r.ariaErrorText,
                    t.props.placeholder = function(e) {
                        return !1 !== e && function(e) {
                            return null != e
                        }(e)
                    }(r.placeholder) ? r.placeholder : t.props.placeholder,
                    t.props.ariaLabel = r.ariaLabel ? r.ariaLabel.toString() : t.props.ariaLabel,
                    t.props.contextualText = r.contextualText,
                    t.isComposing = !1,
                    t.wasComposing = !1,
                    t
                }
                return t = i,
                r = [{
                    key: "init",
                    value: function() {
                        var e = this;
                        if (!this.props.encryptionName || "" === this.props.encryptionName)
                            throw new Error('Error: An "encryptionName" property has not been set on the SF component');
                        this.setBindings(),
                        this.setListeners(),
                        this.specialMessageOnClick = ai,
                        this.specialMessageExternalValidation = ci,
                        this.specialMessageAutoComplete = si,
                        this.processInputFeedback = Io,
                        this.handleErrorOnField = Ko,
                        this.handleInvalidField = Fo,
                        this.handleValidField = qo,
                        this.setDirty = ui,
                        this.unmask = ei,
                        this.validate = function() {
                            throw new Error("Input element does not have a validation function defined.")
                        }
                        ,
                        this.mask = null,
                        this.onAutoFillStart = function(t) {
                            return e.setState({
                                isInAutofillMode: !0
                            }),
                            t.classList.add(gi)
                        }
                        ,
                        this.onAutoFillCancel = function(e) {
                            return e.classList.remove(gi)
                        }
                    }
                }, {
                    key: "setBindings",
                    value: function() {
                        var e = this;
                        this._onKeyDown = this.onKeyDown.bind(this),
                        this._onInput = this.onInput.bind(this),
                        this._onPaste = this.onPaste.bind(this),
                        this._onChange = this.onChangeEvent.bind(this),
                        this._onAnimationStart = this.onAnimationStart.bind(this),
                        this._onCompositionStart = this.onCompositionStart.bind(this),
                        this._onCompositionEnd = this.onCompositionEnd.bind(this),
                        ho.__IS_ANDROID && (this._onKeyUpAndroid = this.onKeyUpAndroid.bind(this)),
                        ho.__IS_IOS && (this._onTouchStart = function() {
                            e.onChange({
                                action: ue,
                                hasGenuineTouchEvents: !0
                            })
                        }
                        ,
                        this._onClick = function() {
                            e.props.disableIOSArrowKeys && e.setState({
                                shouldDisableField: !1
                            })
                        }
                        ,
                        this.specialMessageOnCheckoutTouchEvent = function() {
                            e.props.disableIOSArrowKeys && e.setState({
                                shouldDisableField: !0
                            })
                        }
                        ),
                        this._onFocus = this.onFocus.bind(this),
                        this._onBlur = this.onBlur.bind(this)
                    }
                }, {
                    key: "setListeners",
                    value: function() {
                        L(this.fieldRef, "keydown", this._onKeyDown, !1),
                        L(this.fieldRef, "input", this._onInput, !1),
                        L(this.fieldRef, "paste", this._onPaste, !1),
                        L(this.fieldRef, "change", this._onChange, !1),
                        L(this.fieldRef, "animationstart", this._onAnimationStart, !1),
                        L(this.fieldRef, "compositionstart", this._onCompositionStart, !1),
                        L(this.fieldRef, "compositionend", this._onCompositionEnd, !1),
                        ho.__IS_ANDROID && L(this.fieldRef, "keyup", this._onKeyUpAndroid, !1),
                        ho.__IS_IOS && (L(document, "touchstart", this._onTouchStart),
                        L(document, "click", this._onClick)),
                        L(this.fieldRef, "focus", this._onFocus, !1),
                        L(this.fieldRef, "blur", this._onBlur, !1)
                    }
                }, {
                    key: "onKeyDown",
                    value: function(e) {
                        var t = ii.handleKeyPress(e);
                        this.oldValue = this.fieldRef.value,
                        this.deleteKeyPressed = t === ii.__DELETE_OR_BACKSPACE,
                        this.action = Uo(t, this.desc),
                        this.setState({
                            status: "keyDown"
                        })
                    }
                }, {
                    key: "onInput",
                    value: function() {
                        throw new Error("Subclass must implement an onInput method")
                    }
                }, {
                    key: "onPaste",
                    value: function() {}
                }, {
                    key: "onChangeEvent",
                    value: function(e) {}
                }, {
                    key: "onAnimationStart",
                    value: function(e) {
                        var t = e.target;
                        switch (e.animationName) {
                        case "onautofillstart":
                            return this.onAutoFillStart(t);
                        case "onautofillcancel":
                            return this.onAutoFillCancel(t);
                        default:
                            return null
                        }
                    }
                }, {
                    key: "onKeyUpAndroid",
                    value: function() {}
                }, {
                    key: "onCompositionStart",
                    value: function() {
                        this.isComposing = !0,
                        this.setState({
                            status: "compositionStart",
                            showAsValid: !1
                        })
                    }
                }, {
                    key: "onCompositionEnd",
                    value: function(e) {
                        this.isComposing = !1,
                        ho.__IS_FIREFOX || 10 === ho.__IS_IE || ho.__IS_IE && ho.__IS_IE > 11 ? this.wasComposing = !0 : this.onInput(e, !0)
                    }
                }, {
                    key: "onFocus",
                    value: function() {
                        var e = this.getNumChars();
                        this.hasFocus = !0,
                        this.onChange({
                            action: le,
                            focus: !0,
                            numChars: e
                        })
                    }
                }, {
                    key: "onBlur",
                    value: function(e, t) {
                        var r = this.getNumChars();
                        this.hasFocus = !1,
                        this.onChange({
                            action: le,
                            focus: !1,
                            numChars: r
                        }),
                        t || this.checkIncompleteField()
                    }
                }, {
                    key: "getNumChars",
                    value: function() {
                        return ei(this.fieldRef.value).unmaskedVal.length
                    }
                }, {
                    key: "checkIncompleteField",
                    value: function() {
                        var e = this
                          , t = null;
                        this.fieldRef.value.length && !this.isValidLength && "" === this.state.error && (t = {
                            error: Oe[this.props.fieldType],
                            action: "incorrectly filled field"
                        }),
                        !this.fieldRef.value.length && Se.includes(this.state.error) && (t = {
                            error: "",
                            action: pe
                        }),
                        t && this.processInputFeedback(t).then((function(t) {
                            var r = t.onChangeObj
                              , n = t.stateObj;
                            r && e.onChange(r),
                            e.setState(n)
                        }
                        ))
                    }
                }, {
                    key: "specialMessageOnFocus",
                    value: function() {
                        var e = this;
                        ho.__IS_IOS ? this.setState({
                            shouldDisableField: !1
                        }, (function() {
                            e.onChange({
                                action: ue
                            }),
                            setTimeout((function() {
                                e.fieldRef.focus()
                            }
                            ), 200)
                        }
                        )) : this.fieldRef.focus()
                    }
                }, {
                    key: "specialMessageOnBrand",
                    value: function() {}
                }, {
                    key: "specialMessageOnCode",
                    value: function() {}
                }, {
                    key: "specialMessageExpiryDatePolicy",
                    value: function() {}
                }, {
                    key: "specialMessageUnsupportedCard",
                    value: function() {}
                }, {
                    key: "destroy",
                    value: function() {
                        N(this.fieldRef, "keydown", this._onKeyDown, !1),
                        N(this.fieldRef, "input", this._onInput, !1),
                        N(this.fieldRef, "paste", this._onPaste, !1),
                        N(this.fieldRef, "change", this._onChange, !1),
                        N(this.fieldRef, "animationstart", this._onAnimationStart, !1),
                        N(this.fieldRef, "compositionstart", this._onCompositionStart, !1),
                        N(this.fieldRef, "compositionend", this._onCompositionEnd, !1),
                        ho.__IS_ANDROID && N(this.fieldRef, "keyup", this._onKeyUpAndroid, !1),
                        ho.__IS_IOS && (N(document, "touchstart", this._onTouchStart),
                        N(document, "click", this._onClick)),
                        N(this.fieldRef, "focus", this._onFocus, !1),
                        N(this.fieldRef, "blur", this._onBlur, !1),
                        this.eventLogger && this.eventLogger.destroy()
                    }
                }, {
                    key: "processConfigObjects",
                    value: function(e) {
                        var t, r, n, o = (t = e.fieldType,
                        (r = e.placeholdersConfig) && (t !== J ? Object.prototype.hasOwnProperty.call(r, t) && (n = r[t].toString()) : Object.prototype.hasOwnProperty.call(r, t) ? n = r[t].toString() : (r[z].toString(),
                        r[Y].toString())),
                        {
                            placeholder: n
                        }), i = function(e, t) {
                            var r = {
                                label: void 0,
                                error: void 0,
                                contextualTexts: null
                            }
                              , n = Object.keys(r);
                            return t && Object.prototype.hasOwnProperty.call(t, e) && Object.keys(t[e]).forEach((function(o) {
                                if (n.includes(o)) {
                                    var i = t[e][o];
                                    r[o] = i
                                }
                            }
                            )),
                            r
                        }(e.fieldType, e.ariaConfig), a = function(e, t) {
                            var r = "";
                            return t && (e !== J ? Object.prototype.hasOwnProperty.call(t, e) && (r = t[e].toString()) : Object.prototype.hasOwnProperty.call(t, e) ? r = t[e].toString() : (t[z].toString(),
                            t[Y].toString())),
                            {
                                contextualText: r
                            }
                        }(e.fieldType, i.contextualTexts);
                        return {
                            placeholder: o.placeholder,
                            ariaLabel: i.label,
                            ariaErrorText: i.error,
                            contextualText: a.contextualText
                        }
                    }
                }, {
                    key: "componentDidMount",
                    value: function() {}
                }, {
                    key: "componentDidUpdate",
                    value: function() {}
                }, {
                    key: "componentWillUnmount",
                    value: function() {}
                }, {
                    key: "render",
                    value: function() {
                        throw new Error("Input element cannot be rendered.")
                    }
                }],
                r && fi(t.prototype, r),
                n && fi(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                i
            }(v);
            bi = {
                onChange: function() {}
            },
            (vi = "defaultProps")in (yi = mi) ? Object.defineProperty(yi, vi, {
                value: bi,
                enumerable: !0,
                configurable: !0,
                writable: !0
            }) : yi[vi] = bi;
            function wi(e) {
                return wi = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                wi(e)
            }
            function _i(e, t) {
                var r = null
                  , n = null;
                if ("string" !== wi(e).toLowerCase() && !e) {
                    if (ho.__IS_IE && (10 === ho.__IS_IE || 11 === ho.__IS_IE))
                        return null;
                    r = "",
                    n = de
                }
                if (ho.__IS_IE && (10 === ho.__IS_IE || 11 === ho.__IS_IE) && ("" !== e && "" === t && (r = "",
                n = fe),
                "" === e && "" === t))
                    return null;
                var o = t;
                return /[\uFF10-\uFF19]/g.test(o) && (o = o.replace(/[\uFF10-\uFF19]/g, (function(e) {
                    return String.fromCharCode(e.charCodeAt(0) - 65248)
                }
                ))),
                {
                    oldValue: r,
                    action: n,
                    currentVal: o
                }
            }
            function Oi(e) {
                var t = this.unmask(e);
                Qe(this.extraValidationProps, t);
                var r = this.validate(t)
                  , n = r.newValue
                  , o = r.isValidLength
                  , i = r.error
                  , a = r.propsOnThis
                  , c = r.newCursorPosition
                  , s = r.maxLength
                  , u = r.commObj;
                return i.length ? (Qe(a, this),
                this.setState({
                    status: "onInput_finalised",
                    commObj: u
                }),
                u) : (this.fieldRef.value = n,
                c && ii.setSelectionRange(this.fieldRef, c),
                u = Xe(u, "error", ""),
                u = Xe(u, "action", Uo(this.action, this.desc)),
                this.isValidLength = o,
                this.deleteKeyPressed = !1,
                Qe(a, this),
                this.setState({
                    status: "onInput_finalised",
                    maxLength: s || this.props.maxLength,
                    commObj: u
                }),
                u)
            }
            function Si(e) {
                return Si = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                Si(e)
            }
            function Pi(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            function Ei(e, t) {
                return Ei = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                    return e.__proto__ = t,
                    e
                }
                ,
                Ei(e, t)
            }
            function ki(e) {
                var t = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}
                        ))),
                        !0
                    } catch (e) {
                        return !1
                    }
                }();
                return function() {
                    var r, n = xi(e);
                    if (t) {
                        var o = xi(this).constructor;
                        r = Reflect.construct(n, arguments, o)
                    } else
                        r = n.apply(this, arguments);
                    return function(e, t) {
                        if (t && ("object" === Si(t) || "function" == typeof t))
                            return t;
                        if (void 0 !== t)
                            throw new TypeError("Derived constructors may only return object or undefined");
                        return Ai(e)
                    }(this, r)
                }
            }
            function Ai(e) {
                if (void 0 === e)
                    throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                return e
            }
            function xi(e) {
                return xi = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                    return e.__proto__ || Object.getPrototypeOf(e)
                }
                ,
                xi(e)
            }
            function ji(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            var Ci = function(e) {
                !function(e, t) {
                    if ("function" != typeof t && null !== t)
                        throw new TypeError("Super expression must either be null or a function");
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    Object.defineProperty(e, "prototype", {
                        writable: !1
                    }),
                    t && Ei(e, t)
                }(i, e);
                var t, r, n, o = ki(i);
                function i(e) {
                    var t;
                    !function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, i),
                    ji(Ai(t = o.call(this, e)), "handleFieldRef", (function(e) {
                        t.fieldRef = e
                    }
                    ));
                    var r = t.props.placeholder === Pe ? t.props.placeholder.substr(0, t.props.maxLength) : t.props.placeholder
                      , n = t.props.contextualText;
                    return t.setState({
                        status: "initialising",
                        error: "",
                        showAsValid: !1,
                        ariaInvalid: !1,
                        maxLength: t.props.maxLength,
                        hasUnsupportedCard: !1,
                        ariaRequired: "true",
                        displayPolicy: ve,
                        placeholder: r,
                        contextualText: n,
                        isDirty: !1,
                        shouldDisableField: ho.__IS_IOS && t.props.disableIOSArrowKeys,
                        isInAutofillMode: !1,
                        autofillHasHappened: !1
                    }),
                    t.handleOnInput = Oi,
                    t.desc = t.props.description,
                    t.isValidLength = !1,
                    t.action = "",
                    t.oldValue = void 0,
                    t.deleteKeyPressed = !1,
                    t.valToEncrypt = t.props.valToEncrypt || "fieldRef.value",
                    t.extraFeedbackPropsArr = [],
                    t.extraValidationProps = {},
                    t
                }
                return t = i,
                r = [{
                    key: "onChange",
                    value: function(e) {
                        this.props.onChange(e)
                    }
                }, {
                    key: "componentDidMount",
                    value: function() {
                        this.init(),
                        this.handleValidField = function() {
                            for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                                t[r] = arguments[r];
                            var n = t
                              , o = n.shift();
                            return function() {
                                for (var e = arguments.length, t = new Array(e), r = 0; r < e; r++)
                                    t[r] = arguments[r];
                                return o.apply(this, n.concat(t))
                            }
                        }(this.handleValidField, this.props.encryptionName, this.valToEncrypt, this.extraFeedbackPropsArr),
                        this.props.unmask && (this.unmask = this.props.unmask),
                        this.props.mask && (this.mask = this.props.mask),
                        this.validate = this.props.validate,
                        this.setState({
                            status: "mounted"
                        })
                    }
                }, {
                    key: "onInput",
                    value: function(e, t, r) {
                        if (this.setDirty(),
                        this.isComposing)
                            return {
                                isComposing: !0
                            };
                        var n = _i(this.oldValue, this.fieldRef.value);
                        return n ? (null !== n.oldValue && (this.oldValue = n.oldValue,
                        this.action = n.action),
                        r || this.handleOnInput(n.currentVal, e),
                        n) : {
                            unwantedIEEvent: !0
                        }
                    }
                }, {
                    key: "componentDidUpdate",
                    value: function() {
                        var e = this;
                        if ("onInput_finalised" === this.state.status) {
                            var t = this.state.commObj;
                            t && (this.setState({
                                status: "processing_input"
                            }),
                            this.processInputFeedback(t).then((function(t) {
                                var r = t.onChangeObj
                                  , n = t.stateObj;
                                r && e.onChange(r),
                                e.setState(n)
                            }
                            )))
                        }
                    }
                }, {
                    key: "componentWillUnmount",
                    value: function() {
                        this.destroy(),
                        this.fieldRef = null
                    }
                }, {
                    key: "isHideableField",
                    value: function() {
                        return this.props.fieldType === V || this.props.fieldType === B || this.props.fieldType === G || this.props.fieldType === J
                    }
                }, {
                    key: "render",
                    value: function(e, t, r) {
                        var n, o, i, a = e.fieldType, c = e.autoComplete, s = e.ariaLabel, u = e.legacyInputMode, l = e.uniqueIdFromLabel, f = e.maskSecurityCode, p = t.placeholder, h = t.contextualText, y = t.maxLength, v = t.error, b = t.showAsValid, g = t.ariaInvalid, m = t.ariaRequired, w = t.displayPolicy, _ = t.isDirty, O = t.shouldDisableField, S = "object" !== Si(r) ? r : function() {
                            return null
                        }
                        , P = l || a, E = null === (n = this.props.ariaErrorText) || void 0 === n || null === (o = n[v]) || void 0 === o ? void 0 : o.toString();
                        v && !E && (E = null === (i = this.props.ariaErrorText) || void 0 === i ? void 0 : i[me]);
                        var k = u ? "tel" : "text";
                        f && (k = "password");
                        var A = !v && (null == h ? void 0 : h.length) > 0 ? h : E;
                        return d("div", {
                            className: "gsf-holder",
                            style: "".concat(this.isHideableField() && w === be ? "display: none" : "display: block")
                        }, d("input", {
                            ref: this.handleFieldRef,
                            id: P,
                            "data-fieldtype": a,
                            type: k,
                            inputmode: !u && "numeric",
                            maxlength: y,
                            autocomplete: c,
                            placeholder: p,
                            "aria-label": s,
                            "aria-invalid": _ ? g.toString() : "false",
                            "aria-required": m,
                            "aria-describedby": "".concat(P, "-ariaContext"),
                            style: "display: block",
                            className: "js-iframe-input input-field".concat("" !== v ? " chckt-input-field--error js-chckt-input-field-error" : "").concat(b && _ ? " chckt-input-field--validated js-chckt-input-field-validated" : ""),
                            "data-type": "gsf",
                            readonly: O
                        }), d("span", {
                            className: "aria-error aria-context",
                            id: "".concat(P, "-ariaContext")
                        }, A), d(S, null))
                    }
                }],
                r && Pi(t.prototype, r),
                n && Pi(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                i
            }(mi);
            ji(Ci, "defaultProps", {
                placeholder: Pe,
                ariaLabel: "input field in iframe",
                maxLength: 2,
                encryptionName: "generic"
            });
            const Ri = Ci;
            var Ii = function(e, t, r) {
                if (0 === e || !t.length)
                    return 0;
                var n = t.length - r.length
                  , o = n > 0
                  , i = function(e, t) {
                    return /\s/.test(e.charAt(t))
                }
                  , a = e - n;
                return o && (i(t, a + 1) || i(t, a)) ? e + 1 : !o && i(t, e - 1) ? e - 1 : e
            };
            function Ti(e) {
                var t = e.fieldType
                  , r = e.placeholdersConfig
                  , n = e.ariaConfig
                  , o = e.encryptionKey
                  , i = e.numKey
                  , a = e.legacyInputMode
                  , c = e.uniqueIdFromLabel
                  , s = e.implementationType;
                return {
                    ref: e.handleComponentRef,
                    fieldType: t,
                    placeholdersConfig: r,
                    ariaConfig: n,
                    encryptionKey: o,
                    numKey: i,
                    onChange: e.onChange,
                    legacyInputMode: a,
                    uniqueIdFromLabel: c,
                    implementationType: s,
                    disableIOSArrowKeys: e.disableIOSArrowKeys
                }
            }
            var Di = ["fieldType", "extraFieldData", "placeholdersConfig"];
            function Ki() {
                return Ki = Object.assign ? Object.assign.bind() : function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = arguments[t];
                        for (var n in r)
                            Object.prototype.hasOwnProperty.call(r, n) && (e[n] = r[n])
                    }
                    return e
                }
                ,
                Ki.apply(this, arguments)
            }
            function Fi(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Mi(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Fi(Object(r), !0).forEach((function(t) {
                        Hi(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Fi(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function Hi(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Ui(e, t) {
                if (null == e)
                    return {};
                var r, n, o = function(e, t) {
                    if (null == e)
                        return {};
                    var r, n, o = {}, i = Object.keys(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || (o[r] = e[r]);
                    return o
                }(e, t);
                if (Object.getOwnPropertySymbols) {
                    var i = Object.getOwnPropertySymbols(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || Object.prototype.propertyIsEnumerable.call(e, r) && (o[r] = e[r])
                }
                return o
            }
            const Li = function(e, t, r, n) {
                var o, i, a, c, s, u = e.fieldType, l = e.extraFieldData, f = e.placeholdersConfig, p = Ui(e, Di);
                !function(e) {
                    if (null == e)
                        throw new TypeError("Cannot destructure " + e)
                }(t);
                var h = "maxLength"
                  , y = Mi({}, f)
                  , v = qe(l, "maskInterval");
                +v && (s = (s = +v) > 0 || !Number.isNaN(s) ? s : null);
                var b = qe(l, "length");
                if (b && ("number" == typeof b && (a = (a = l.length) > 0 ? a : null),
                "string" == typeof b)) {
                    var g = function(e) {
                        var t = null
                          , r = null
                          , n = e.replace(/[^\d\-|]/g, "")
                          , o = e.replace(/[^\-|]/g, "").substr(0, 1)
                          , i = n.match(/\d+/g);
                        if (!i)
                            return {
                                startVal: t,
                                endVal: r,
                                separatorStr: o
                            };
                        var a = i.map((function(e) {
                            return +e
                        }
                        )).filter((function(e, t, r) {
                            return r.indexOf(e) === t && e > 0
                        }
                        )).reduce((function(e, t) {
                            return e.length < 2 && e.push(t),
                            e
                        }
                        ), []).sort((function(e, t) {
                            return e - t
                        }
                        ));
                        return a.length ? 1 === a.length ? {
                            startVal: t,
                            endVal: r = a[0],
                            separatorStr: o
                        } : {
                            startVal: t = a[0],
                            endVal: r = a[1],
                            separatorStr: o
                        } : {
                            startVal: t,
                            endVal: r,
                            separatorStr: o
                        }
                    }(b)
                      , m = g.startVal
                      , w = g.endVal
                      , _ = g.separatorStr;
                    a = w,
                    (c = m) && a && _.length && (h = _.indexOf("|") > -1 ? "twoStops" : "range")
                }
                s && (i = function(e) {
                    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : " "
                      , r = new RegExp("(.{".concat(e, "})(?!$)"),"g");
                    return function(e) {
                        return e.replace(/\W/gi, "").replace(r, "$1".concat(t)).trim()
                    }
                }(s),
                a && (a += ti(a, s)),
                c && (c += ti(c, s)));
                var O, S = a || 2;
                switch (u) {
                case "encryptedCardNumber":
                    o = "giftCardNumber";
                    break;
                case "encryptedSecurityCode":
                    o = "giftCardPin";
                    break;
                default:
                    o = (O = u.substr(9)).charAt(0).toLowerCase() + O.slice(1)
                }
                var P = function(e, t) {
                    var r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : "maxLength";
                    return function(n) {
                        var o = n.unmaskedVal
                          , i = !1
                          , a = t || e
                          , c = o
                          , s = this.mask ? this.mask(c) : c
                          , u = null;
                        if (this.mask) {
                            var l = this.fieldRef.selectionStart
                              , f = this.oldValue;
                            u = Ii(l, s, f)
                        }
                        switch (r) {
                        case "range":
                            s.length >= a && s.length <= e && (i = !0);
                            break;
                        case "twoStops":
                            s.length !== a && s.length !== e || (i = !0);
                            break;
                        default:
                            s.length === e && (i = !0)
                        }
                        return {
                            newValue: s,
                            isValidLength: i,
                            commObj: {},
                            error: "",
                            newCursorPosition: u
                        }
                    }
                }(S, c, h);
                y[u] || "" === y[u] || (y[u] = s ? i(Pe).substr(0, S) : Pe.substr(0, S));
                var E = Ti(Mi({
                    handleComponentRef: r,
                    onChange: n,
                    fieldType: u
                }, p));
                return d(Ri, Ki({}, E, {
                    placeholdersConfig: y,
                    description: "digits",
                    encryptionName: o,
                    mask: i,
                    unmask: undefined,
                    validate: P,
                    maxLength: S,
                    autoComplete: undefined,
                    valToEncrypt: undefined
                }))
            };
            function Ni(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function Wi(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var r = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? Ni(Object(r), !0).forEach((function(t) {
                        Vi(e, t, r[t])
                    }
                    )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : Ni(Object(r)).forEach((function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                    }
                    ))
                }
                return e
            }
            function Vi(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function Bi(e, t, r, n, o, i, a) {
                try {
                    var c = e[i](a)
                      , s = c.value
                } catch (e) {
                    return void r(e)
                }
                c.done ? t(s) : Promise.resolve(s).then(n, o)
            }
            function Gi() {
                return Ji.apply(this, arguments)
            }
            function Ji() {
                var e;
                return e = regeneratorRuntime.mark((function e() {
                    var t, r, n, o, i, a, c;
                    return regeneratorRuntime.wrap((function(e) {
                        for (; ; )
                            switch (e.prev = e.next) {
                            case 0:
                                return t = this.props.fieldType,
                                r = {
                                    valToEncrypt: this.separateDateValues[0],
                                    encryptionType: "month",
                                    encryptionKey: this.props.encryptionKey,
                                    encryptionName: $,
                                    fieldType: t
                                },
                                e.next = 4,
                                Yo(r);
                            case 4:
                                return (n = e.sent) || console.warn("### handleValidDateField::ENCRYPTION FAIL:: encryptedMonthObj=", n),
                                o = Wi(Wi({}, r), {}, {
                                    valToEncrypt: this.separateDateValues[1],
                                    encryptionType: "year",
                                    encryptionName: q
                                }),
                                e.next = 9,
                                Yo(o);
                            case 9:
                                if ((i = e.sent) || console.warn("### handleValidDateField::ENCRYPTION FAIL:: encryptedYearObj=", i),
                                !n || !i) {
                                    e.next = 17;
                                    break
                                }
                                return a = i[V],
                                (c = n[V] && n[V][0]) && a.unshift(c),
                                !0 === this.exposeExpiryDate && (i.expiryDate = "".concat(this.separateDateValues[0], "/").concat(this.separateDateValues[1])),
                                e.abrupt("return", {
                                    onChangeObj: i,
                                    stateObj: {
                                        showAsValid: !0,
                                        ariaInvalid: !1,
                                        error: ""
                                    }
                                });
                            case 17:
                                return console.warn("### handleValidDateField:: ENCRYPTION FAIL"),
                                e.abrupt("return", {});
                            case 19:
                            case "end":
                                return e.stop()
                            }
                    }
                    ), e, this)
                }
                )),
                Ji = function() {
                    var t = this
                      , r = arguments;
                    return new Promise((function(n, o) {
                        var i = e.apply(t, r);
                        function a(e) {
                            Bi(i, n, o, a, c, "next", e)
                        }
                        function c(e) {
                            Bi(i, n, o, a, c, "throw", e)
                        }
                        a(void 0)
                    }
                    ))
                }
                ,
                Ji.apply(this, arguments)
            }
            function zi(e) {
                return zi = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                    return typeof e
                }
                : function(e) {
                    return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                }
                ,
                zi(e)
            }
            function Yi(e, t) {
                for (var r = 0; r < t.length; r++) {
                    var n = t[r];
                    n.enumerable = n.enumerable || !1,
                    n.configurable = !0,
                    "value"in n && (n.writable = !0),
                    Object.defineProperty(e, n.key, n)
                }
            }
            function $i() {
                return $i = "undefined" != typeof Reflect && Reflect.get ? Reflect.get.bind() : function(e, t, r) {
                    var n = function(e, t) {
                        for (; !Object.prototype.hasOwnProperty.call(e, t) && null !== (e = Qi(e)); )
                            ;
                        return e
                    }(e, t);
                    if (n) {
                        var o = Object.getOwnPropertyDescriptor(n, t);
                        return o.get ? o.get.call(arguments.length < 3 ? e : r) : o.value
                    }
                }
                ,
                $i.apply(this, arguments)
            }
            function qi(e, t) {
                return qi = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(e, t) {
                    return e.__proto__ = t,
                    e
                }
                ,
                qi(e, t)
            }
            function Xi(e) {
                var t = function() {
                    if ("undefined" == typeof Reflect || !Reflect.construct)
                        return !1;
                    if (Reflect.construct.sham)
                        return !1;
                    if ("function" == typeof Proxy)
                        return !0;
                    try {
                        return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function() {}
                        ))),
                        !0
                    } catch (e) {
                        return !1
                    }
                }();
                return function() {
                    var r, n = Qi(e);
                    if (t) {
                        var o = Qi(this).constructor;
                        r = Reflect.construct(n, arguments, o)
                    } else
                        r = n.apply(this, arguments);
                    return function(e, t) {
                        if (t && ("object" === zi(t) || "function" == typeof t))
                            return t;
                        if (void 0 !== t)
                            throw new TypeError("Derived constructors may only return object or undefined");
                        return function(e) {
                            if (void 0 === e)
                                throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                            return e
                        }(e)
                    }(this, r)
                }
            }
            function Qi(e) {
                return Qi = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(e) {
                    return e.__proto__ || Object.getPrototypeOf(e)
                }
                ,
                Qi(e)
            }
            var Zi = function(e) {
                !function(e, t) {
                    if ("function" != typeof t && null !== t)
                        throw new TypeError("Super expression must either be null or a function");
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            writable: !0,
                            configurable: !0
                        }
                    }),
                    Object.defineProperty(e, "prototype", {
                        writable: !1
                    }),
                    t && qi(e, t)
                }(i, e);
                var t, r, n, o = Xi(i);
                function i(e) {
                    var t;
                    return function(e, t) {
                        if (!(e instanceof t))
                            throw new TypeError("Cannot call a class as a function")
                    }(this, i),
                    (t = o.call(this, e)).separateDateValues = [],
                    t.oldCursor = void 0,
                    t.newCursorPosition = void 0,
                    t.extraValidationProps = {
                        minimumExpiryDateStr: t.props.minimumExpiryDate
                    },
                    t.exposeExpiryDate = t.props.exposeExpiryDate,
                    t.setState({
                        status: "initialising",
                        ariaRequired: t.props.expiryDatePolicy === ge ? "true" : "false"
                    }),
                    t
                }
                return t = i,
                r = [{
                    key: "componentDidMount",
                    value: function() {
                        $i(Qi(i.prototype), "componentDidMount", this).call(this),
                        this.handleValidField = Gi
                    }
                }, {
                    key: "onKeyDown",
                    value: function(e) {
                        this.oldCursor = ii.getCaretPos(this.fieldRef, !0),
                        $i(Qi(i.prototype), "onKeyDown", this).call(this, e)
                    }
                }, {
                    key: "onKeyUpAndroid",
                    value: function() {
                        this.newCursorPosition === this.fieldRef.value.length && ii.setSelectionRange(this.fieldRef, this.newCursorPosition)
                    }
                }, {
                    key: "getNumChars",
                    value: function() {
                        var e = $i(Qi(i.prototype), "getNumChars", this).call(this);
                        return this.fieldRef.value.length >= 3 && (e += 1),
                        e
                    }
                }, {
                    key: "specialMessageExpiryDatePolicy",
                    value: function(e) {
                        this.setState({
                            status: "expiryDatePolicyMsg_processed",
                            ariaRequired: e.expiryDatePolicy === ge ? "true" : "false",
                            displayPolicy: e.expiryDatePolicy
                        })
                    }
                }],
                r && Yi(t.prototype, r),
                n && Yi(t, n),
                Object.defineProperty(t, "prototype", {
                    writable: !1
                }),
                i
            }(Ri);
            !function(e, t, r) {
                t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r
            }(Zi, "defaultProps", {
                placeholder: "MM/YY",
                ariaLabel: "Expiry date"
            });
            const ea = Zi;
            const ta = function() {
                var e = arguments.length > 2 && void 0 !== arguments[2] && arguments[2]
                  , t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : ""
                  , r = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "";
                t.length > 2 && (r = (r = t.substring(2) + r).substring(0, 2),
                t = t.substring(0, 2));
                var n = Number(t);
                return 1 === t.length && (n >= 2 && n <= 9 || e) && (t = "0".concat(n)),
                2 === t.length && (0 === n && (t = "01"),
                n > 12 && (r = (r = t.substring(1) + r).substring(0, 2),
                t = "0".concat(t.substring(0, 1)))),
                {
                    typedMonth: t,
                    typedYear: r
                }
            };
            const ra = function(e, t, r, n) {
                var o = ""
                  , i = ""
                  , a = r.getFullYear()
                  , c = "20".concat(t)
                  , s = Number(c)
                  , u = Number(e)
                  , l = new Date(s,u - 1)
                  , f = new Date(a,r.getMonth() - 3);
                if (l.getTime() < f)
                    return {
                        value: o = Qo(e + t),
                        error: i = "error.va.sf-cc-dat.01"
                    };
                if (s > a + Q)
                    return {
                        value: o = Qo(e + t),
                        error: i = "error.va.sf-cc-dat.02"
                    };
                var p = function(e, t) {
                    var r = null;
                    if (!e)
                        return r;
                    if (e) {
                        var n = e.split(X);
                        if (n[0].length < 1 || n[0].length > 2 || n[1].length < 2 || 3 === n[1].length || n[1].length > 4)
                            return r;
                        var o = n[0]
                          , i = 2 === n[1].length ? "20".concat(n[1]) : n[1];
                        return i > t + Q ? r : r = new Date(Number(i),Number(o) - 1)
                    }
                    return r
                }(n, a);
                return p && l.getTime() < p.getTime() ? {
                    value: o = Qo(e + t),
                    error: i = "error.va.sf-cc-dat.03"
                } : {
                    value: o,
                    error: i
                }
            };
            function na(e) {
                var t, r, n = e.originalVal, o = e.dateArr, i = e.cursorPosFlag, a = e.minimumExpiryDateStr, c = !1, s = 1 === this.oldValue.length && Mo(n) === X, u = {}, l = new Date(genTime), f = ta(o[0], o[1], s), p = f.typedMonth, d = f.typedYear;
                if (d && 2 === d.length) {
                    var h = ra(p, d, l, a)
                      , y = h.value
                      , v = h.error;
                    if (y.length && (this.fieldRef.value = y),
                    v.length)
                        return (u = Xe(u, "error", v)).action = Uo(this.action, "date"),
                        {
                            error: v,
                            commObj: u,
                            propsOnThis: {
                                separateDateValues: []
                            }
                        }
                }
                2 === (t = this.mask(p + d)).length && Mo(t) === X && (t = Ho(t, 1)),
                "" !== t && this.deleteKeyPressed && ii.getCaretPos(this.fieldRef) === n.length && 2 === ii.getCaretPos(this.fieldRef) && (t = Ho(t, 2)),
                5 === t.length && (c = !0),
                i && (r = i);
                var b = this.unmask(t).dateArr
                  , g = [b[0] && 2 === b[0].length ? b[0] : "", b[1] && 2 === b[1].length ? "20".concat(b[1]) : ""]
                  , m = g[1]
                  , w = 4 === (null == m ? void 0 : m.length) && !Number.isNaN(parseInt(m));
                return "" !== g[0] && w || (c = !1),
                {
                    newValue: t,
                    isValidLength: c,
                    commObj: u,
                    error: "",
                    newCursorPosition: r,
                    propsOnThis: {
                        newCursorPosition: r,
                        separateDateValues: g
                    }
                }
            }
            var oa = ["minimumExpiryDate", "expiryDatePolicy", "exposeExpiryDate"];
            function ia() {
                return ia = Object.assign ? Object.assign.bind() : function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = arguments[t];
                        for (var n in r)
                            Object.prototype.hasOwnProperty.call(r, n) && (e[n] = r[n])
                    }
                    return e
                }
                ,
                ia.apply(this, arguments)
            }
            function aa(e, t) {
                var r = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var n = Object.getOwnPropertySymbols(e);
                    t && (n = n.filter((function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable
                    }
                    ))),
                    r.push.apply(r, n)
                }
                return r
            }
            function ca(e, t, r) {
                return t in e ? Object.defineProperty(e, t, {
                    value: r,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = r,
                e
            }
            function sa(e, t) {
                if (null == e)
                    return {};
                var r, n, o = function(e, t) {
                    if (null == e)
                        return {};
                    var r, n, o = {}, i = Object.keys(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || (o[r] = e[r]);
                    return o
                }(e, t);
                if (Object.getOwnPropertySymbols) {
                    var i = Object.getOwnPropertySymbols(e);
                    for (n = 0; n < i.length; n++)
                        r = i[n],
                        t.indexOf(r) >= 0 || Object.prototype.propertyIsEnumerable.call(e, r) && (o[r] = e[r])
                }
                return o
            }
            const ua = function(e, t, r, n) {
                var o = e.minimumExpiryDate
                  , i = e.expiryDatePolicy
                  , a = e.exposeExpiryDate
                  , c = sa(e, oa);
                !function(e) {
                    if (null == e)
                        throw new TypeError("Cannot destructure " + e)
                }(t);
                var s = Ti(function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var r = null != arguments[t] ? arguments[t] : {};
                        t % 2 ? aa(Object(r), !0).forEach((function(t) {
                            ca(e, t, r[t])
                        }
                        )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(r)) : aa(Object(r)).forEach((function(t) {
                            Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(r, t))
                        }
                        ))
                    }
                    return e
                }({
                    handleComponentRef: r,
                    onChange: n
                }, c));
                return d(ea, ia({}, s, {
                    description: "date",
                    encryptionName: "n/a",
                    mask: Qo,
                    unmask: Zo,
                    validate: na,
                    maxLength: 5,
                    autoComplete: "cc-exp",
                    minimumExpiryDate: o,
                    expiryDatePolicy: i,
                    exposeExpiryDate: a
                }))
            };
            const la = function(e, t) {
                var r = e.fieldType;
                return function(e) {
                    if (null == e)
                        throw new TypeError("Cannot destructure " + e)
                }(t),
                d("input", {
                    className: "input-field",
                    style: "display:block;color:red;",
                    value: "Undefined SF type: ".concat(r),
                    readOnly: !0
                })
            };
            var fa = {
                encryptedCardNumber: Li,
                encryptedSecurityCode: Li,
                encryptedExpiryDate: ua,
                default: la
            };
            Array.prototype.includes || Object.defineProperty(Array.prototype, "includes", {
                value: function(e, t) {
                    if (null == this)
                        throw new TypeError('"this" is null or not defined');
                    var r = Object(this)
                      , n = r.length >>> 0;
                    if (0 === n)
                        return !1;
                    var o = 0 | t
                      , i = Math.max(o >= 0 ? o : n - Math.abs(o), 0);
                    function a(e, t) {
                        return e === t || "number" == typeof e && "number" == typeof t && isNaN(e) && isNaN(t)
                    }
                    for (; i < n; ) {
                        if (a(r[i], e))
                            return !0;
                        i++
                    }
                    return !1
                }
            }),
            Object.entries || (Object.entries = function(e) {
                for (var t = Object.keys(e), r = t.length, n = new Array(r); r--; )
                    n[r] = [t[r], e[t[r]]];
                return n
            }
            ),
            Array.prototype.fill || Object.defineProperty(Array.prototype, "fill", {
                value: function(e) {
                    if (null == this)
                        throw new TypeError("this is null or not defined");
                    for (var t = Object(this), r = t.length >>> 0, n = arguments[1] >> 0, o = n < 0 ? Math.max(r + n, 0) : Math.min(n, r), i = arguments[2], a = void 0 === i ? r : i >> 0, c = a < 0 ? Math.max(r + a, 0) : Math.min(a, r); o < c; )
                        t[o] = e,
                        o++;
                    return t
                }
            }),
            Ro((function(e, t, r, n) {
                var o = fa[t.status] || fa.default;
                return o ? o(e, t, r, n) : null
            }
            ), "giftcard"),
            window.sfVersion = "4.9.0"
        }
        )()
    }
    )();

}
)();