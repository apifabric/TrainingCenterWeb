import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InstructorAssignmentHomeComponent } from './home/InstructorAssignment-home.component';
import { InstructorAssignmentNewComponent } from './new/InstructorAssignment-new.component';
import { InstructorAssignmentDetailComponent } from './detail/InstructorAssignment-detail.component';

const routes: Routes = [
  {path: '', component: InstructorAssignmentHomeComponent},
  { path: 'new', component: InstructorAssignmentNewComponent },
  { path: ':id', component: InstructorAssignmentDetailComponent,
    data: {
      oPermission: {
        permissionId: 'InstructorAssignment-detail-permissions'
      }
    }
  }
];

export const INSTRUCTORASSIGNMENT_MODULE_DECLARATIONS = [
    InstructorAssignmentHomeComponent,
    InstructorAssignmentNewComponent,
    InstructorAssignmentDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InstructorAssignmentRoutingModule { }