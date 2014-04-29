# -*- coding: utf-8 -*-

from etree_typo import Typograph
import unittest

def highlight(txt):
    return txt.replace(u'\u00a0', u'␣')\
              .replace(u'\N{NON-BREAKING HYPHEN}', u'=')

class RuTests(unittest.TestCase):

    def assertText(self, text, *args):
        value = Typograph.typograph_text(text, 'ru')
        value_hl = highlight(value)
        if not value_hl in args:
            print '\n'
            print value_hl
            for arg in args:
                print arg
            print '\n'
        self.assertIn(value_hl, args)

        value2 = Typograph.typograph_html(value, 'ru')
        if value != value2:
            print '\n', highlight(value), '\n', highlight(value2)
        self.assertEqual(highlight(value), highlight(value2))

    def assertHtml(self, text, *args):
        value = Typograph.typograph_html(text, 'ru')
        value_hl = highlight(value)
        if not value_hl in args:
            print '\n'
            print value_hl
            for arg in args:
                print arg
            print '\n'
        self.assertIn(value_hl, args)

        value2 = Typograph.typograph_html(value, 'ru')
        if value != value2:
            print '\n', highlight(value), '\n', highlight(value2)
        self.assertEqual(highlight(value), highlight(value2))

    # XXX cleanup tests

    def test_1(self):
        self.assertText(
            u'Кролики -  это   не только ценный мех, но и 3-4 кг ценного мяса',
            u'Кролики␣— это не␣только ценный мех, но␣и␣3‒4 кг ценного мяса')

    def test_2(self):
        self.assertText(
            u'Если бы люди летали как птицы...',
            u'Если␣бы люди летали как птицы…')

    def test_3(self):
        self.assertText(
            u'А в ответ ему: "Таити, Таити! Не были мы на вашем "Таити"!".',
            u'А␣в␣ответ ему: «Таити, Таити! Не␣были мы␣на␣вашем „Таити“!».')

    def test_3_1(self):
        self.assertText(
            u'А в ответ ему: «Таити, Таити! Не были мы на вашем «Таити»!».',
            u'А␣в␣ответ ему: «Таити, Таити! Не␣были мы␣на␣вашем „Таити“!».')

    def test_4(self):
        self.assertText(
            u'Оно было светло-красного цвета и \N{RIGHT DOUBLE QUOTATION MARK}улыбалось" по-доброму.',
            u'Оно было светло-красного цвета и␣„улыбалось“ по=доброму.')

    def test_5(self):
        self.assertText(
            u'- Во-первых, 20 июня 2000 года был ненастный понедельник, - ответил он. '
                u'- Во-вторых, было уже поздно, а в-третьих, я уже был дома. '
                u'Вы меня кое-с-кем перепутали. Как-то так.',
            u'— Во=первых, 20␣июня 2000␣года был ненастный понедельник,␣— ответил он.␣'
                u'— Во=вторых, было уже поздно, а␣в=третьих, я␣уже был дома. '
                u'Вы␣меня кое=с=кем перепутали. Как=то так.')


    def test_6(self):
        self.assertText(
            u'Авторы: к.т.н. Петров, к.ф.-м.н. Иванов, д. х.  н. Васильев и т. д. и т. п.',
            u'Авторы: к.␣т.␣н. Петров, к.␣ф.␣=м.␣н. Иванов, д.␣х.␣н. Васильев и␣т.␣д. и␣т.␣п.')

    def test_7(self):
        self.assertHtml(
            u'<p>- Да!</p><p>- Нет!</p>',
            u'<p>— Да!</p><p>— Нет!</p>')

    def test_8(self):
        self.assertHtml(
            u'<p><b>Ученье </b>- свет!</p>',
            u'<p><b>Ученье␣</b>— свет!</p>')

    def test_9(self):
        self.assertHtml(
            u'<p><b>Неученье </b> - тьма!</p>',
            u'<p><b>Неученье</b>␣— тьма!</p>',
            u'<p><b>Неученье␣</b>— тьма!</p>')
