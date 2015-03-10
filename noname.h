///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun  5 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/button.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/statbmp.h>
#include <wx/animate.h>
#include <wx/combobox.h>
#include <wx/choice.h>
#include <wx/sizer.h>
#include <wx/dialog.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class Lottery_GUI
///////////////////////////////////////////////////////////////////////////////
class Lottery_GUI : public wxDialog 
{
	private:
	
	protected:
		wxButton* m_button1;
		wxButton* m_button2;
		wxStaticBitmap* m_bitmap1;
		wxAnimationCtrl* m_animCtrl1;
		wxComboBox* m_comboBox1;
		wxChoice* m_choice1;
	
	public:
		
		Lottery_GUI( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 362,443 ), long style = wxDEFAULT_DIALOG_STYLE ); 
		~Lottery_GUI();
	
};

#endif //__NONAME_H__
