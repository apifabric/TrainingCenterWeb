import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {COURSE_MODULE_DECLARATIONS, CourseRoutingModule} from  './Course-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CourseRoutingModule
  ],
  declarations: COURSE_MODULE_DECLARATIONS,
  exports: COURSE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CourseModule { }