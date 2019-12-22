
import ui
import console
import traceback

def checkBoxAction(switch):
  print(  'switchActionOnce.switch.value   = <{0:2d}>'.format(switch.value  ))
  if switch.value:
    switch.enabled = 0
  print(  'switch.enabled = <{0:2d}>'.format(switch.enabled))

def numberAction(text):
  pass

def EmptyCell():
  cell = ui.TableViewCell()
  
  l = ui.Label()
  l.text = 'EmptyCell'
  l.frame = ( 12, 0, 150, 25)
  cell.content_view.add_subview(l)
  
  return cell

def CheckBox(prompt):
  cell = ui.TableViewCell()

  l = ui.Label()
  l.text = prompt
  l.frame = ( 12, 0, 150, 25)
  cell.content_view.add_subview(l)
  
  s = ui.Switch()
  s.prompt = prompt
  s.value = 0
  s.action = checkBoxAction
  s.frame = (160, 0,  75, 25)
  cell.content_view.add_subview(s)

  return cell


def Number(prompt, defaultValue):
  cell = ui.TableViewCell()

  l = ui.Label()
  l.text = prompt
  l.frame = ( 12, 0, 150, 25)
  cell.content_view.add_subview(l)
    
  s = ui.TextField()
  s.prompt = prompt
  s.text = repr(defaultValue)
  s.action = numberAction
  s.frame = (160, 0,  75, 25)
  cell.content_view.add_subview(s)

  return cell

class makeTableView(object):

  def tableview_number_of_sections(self, tableview):
    return 1

  def tableview_number_of_rows(self, tableview, section):
    return 9

  def tableview_cell_for_row(self, tableview, section, row):
    if row == 0:
      cell = CheckBox('speed')
    elif row == 1:
      cell = CheckBox('AM pills')
    elif row == 2:
      cell = Number('AM Lantus',25)
    elif row == 3:
      cell = Number('AM Humalog',0)
    elif row == 6:
      cell = CheckBox('PM pills')
    elif row == 7:
      cell = Number('PM Lantus',45)
    elif row == 8:
      cell = Number('PM Humalog',0)
    else:
      cell = EmptyCell()
    return cell

  def tableview_title_for_header(self, tableview, section):
    return 'Daily Tasks'

  def tableview_can_delete(self, tableview, section, row):
    return False

  def tableview_can_move(self, tableview, section, row):
    return False

  def tableview_delete(self, tableview, section, row):
    pass

  def tableview_move_row(self, tableview, from_section, from_row, to_section,
                         to_row):
    pass


t = ui.TableView()
t.frame = (2, 2, 350, 280)
t.border_width = 1
t.border_color = 'black'
t.data_source = makeTableView()
t.present('sheet')
