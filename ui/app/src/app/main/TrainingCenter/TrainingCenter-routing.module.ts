import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrainingCenterHomeComponent } from './home/TrainingCenter-home.component';
import { TrainingCenterNewComponent } from './new/TrainingCenter-new.component';
import { TrainingCenterDetailComponent } from './detail/TrainingCenter-detail.component';

const routes: Routes = [
  {path: '', component: TrainingCenterHomeComponent},
  { path: 'new', component: TrainingCenterNewComponent },
  { path: ':id', component: TrainingCenterDetailComponent,
    data: {
      oPermission: {
        permissionId: 'TrainingCenter-detail-permissions'
      }
    }
  },{
    path: ':training_center_id/Course', loadChildren: () => import('../Course/Course.module').then(m => m.CourseModule),
    data: {
        oPermission: {
            permissionId: 'Course-detail-permissions'
        }
    }
}
];

export const TRAININGCENTER_MODULE_DECLARATIONS = [
    TrainingCenterHomeComponent,
    TrainingCenterNewComponent,
    TrainingCenterDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingCenterRoutingModule { }