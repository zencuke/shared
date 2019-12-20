
import ui
 
def switchActionOnce(val):
  print(  'switchActionOnce.value   = <{0:2d}>'.format(val.value  ))
  if val.value:
    val.enabled = 0
  print(  'switchActionOnce.enabled = <{0:2d}>'.format(val.enabled))

def switchAction(val):
  print(  'switchAction.value       = <{0:2d}>'.format(val.value  ))

class MockTableCellType(type):
  def __instancecheck__(self, other):
    if other == ui.TableViewCell:
      return True

class EmptyCell(object):
  __metaclass__ = MockTableCellType

  def __new__(cls):
    ce = ui.TableViewCell()
    v = ui.View(bg_color=(0.5,0.5,0.5,.1),
                frame=ce.content_view.bounds)

    l = ui.Label()
    l.text = 'EmptyCell'
    l.frame = ( 12, 0, 150, 25)
    v.add_subview(l)
    
    ce.content_view.add_subview(v)
    return ce

class CheckBox(object):
  __metaclass__ = MockTableCellType

  def __new__(cls, prompt):
    cs = ui.TableViewCell()

    l = ui.Label()
    l.text = prompt
    l.frame = ( 12, 0, 150, 25)
    cs.content_view.add_subview(l)
    
    s = ui.Switch()
    s.value = 0
    action = lambda val: cls.checkAction(<val)
    s.action = action
    s.frame = (160, 0,  75, 25)
    cs.content_view.add_subview(s)
    return cs
  
  def checkAction(self, val):
    print(val)
    

class Number(object):
  __metaclass__ = MockTableCellType

  def __new__(cls, prompt, defaultValue):
    cs = ui.TableViewCell()

    l = ui.Label()
    l.text = prompt
    l.frame = ( 12, 0, 150, 25)
    cs.content_view.add_subview(l)
    
    s = ui.TextField()
    s.text = repr(defaultValue)
    s.action = lambda val: switchActionOnce(val)
    s.frame = (160, 0,  75, 25)
    cs.content_view.add_subview(s)
    return cs

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
      cell = Number('AM lantus',25)
    elif row == 7:
      cell = CheckBox('PM pill')
    elif row == 8:
      cell = Number('PM lantus',45)
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
t.frame = (2, 2, 150, 280)
t.border_width = 1
t.border_color = 'black'
t.data_source = makeTableView()
t.present('sheet')

