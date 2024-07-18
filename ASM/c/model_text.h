#ifndef MODEL_TEXT_H
#define MODEL_TEXT_H

#include "gfx.h"
#include "text.h"
#include "util.h"
#include "z64.h"

extern uint16_t illegal_model;

void draw_illegal_model_text(z64_disp_buf_t* db);
void check_model_skeletons();

#endif
